from django.http import Http404
from django.shortcuts import render

import helpers
from courses import services


def course_list_view(request):
    queryset = services.get_publish_courses()
    context = {'object_list': queryset}
    template_name = 'courses/list.html'
    if request.htmx:
        template_name = 'courses/snippets/list-display.html'
        context['queryset'] = queryset[:3]
    return render(request, template_name, context)


def course_detail_view(request, course_id=None, *args, **kwargs):
    course_obj = services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404
    lessons_queryset = services.get_course_lessons(course_obj)
    context = {'object': course_obj, 'lessons_queryset': lessons_queryset}
    # return JsonResponse({
    #     'data': course_obj.id,
    #     'lesson_ids': [x.path for x in lessons_queryset],
    # })
    return render(request, 'courses/detail.html', context)


def lesson_detail_view(
    request, course_id=None, lesson_id=None, *args, **kwargs
):
    lesson_obj = services.get_lesson_detail(
        course_id=course_id, lesson_id=lesson_id
    )
    if lesson_obj is None:
        raise Http404
    email_id_exists = request.session.get('email_id')
    if lesson_obj.requires_email and not email_id_exists:
        request.session['next_url'] = request.path
        return render(request, 'courses/email-required.html', {})
    template_name = 'courses/lesson-coming-soon.html'
    context = {'object': lesson_obj}
    if not lesson_obj.is_coming_soon and lesson_obj.has_video:
        template_name = 'courses/lesson.html'
        video_embed_html = helpers.get_cloudinary_video_object(
            lesson_obj, field_name='video', width=1250, as_html=True
        )
        context['video_embed'] = video_embed_html
    return render(request, template_name, context)
