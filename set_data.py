from random import randint

from django.core.files import File

# locale imports
from about_us.models import ContactInfoModel

from course_projects.models import CourseModel, CourseProjectModel

from news.models import ParagraphModel, NewsItemModel

from library.models import BookModel

from students.models import StudentModel

from demo_exam.models import ResultModel

from practice.models import PracticeModel


def create_about_us_model():
    contact_info = ContactInfoModel(
        email='kirill9366@gmail.com',
        phone='89508204525',
        location='Страна Россия г. Ижевск ул. Максима Горького 222',
        vkontakte='https://vk.com/sdf',
        description="""
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
            Описание Описание Описание Описание Описание Описание 
        """, # noqa
    )
    contact_info.image.save(
        f'image_{randint(0,2000)}.png',
        File(open('static/images/profile_photo.png', 'rb')),
    )
    contact_info.save()


def create_paragraph_model(quantity=3):
    return [ParagraphModel.objects.create(
        title='Some title',
        text="""
            Some text Some text Some text Some text 
            Some text Some text Some text Some text 
            Some text Some text Some text Some text 
            Some text Some text Some text Some text 
            Some text Some text Some text Some text 
        """, # noqa
    ) for i in range(0, quantity)]


def create_course_model():
    for i in range(2, 5):
        CourseModel.objects.create(number=i)


def create_course_projects():
    paragraphs = create_paragraph_model()
    course = CourseModel.objects.get(number=2)
    course_project = CourseProjectModel(
        title='Course Project',
        subtitle='Subtitle of course project',
        course=course,
    )
    course_project.image.save(
        f'image_{randint(0,2000)}.png',
        File(open('static/images/profile_photo.png', 'rb')),
    )
    course_project.save()

    for paragraph in paragraphs:
        course_project.content.add(paragraph)


def create_books():
    for i in range(1, 9):
        book = BookModel.objects.create(
            title=f'Категория {i}',
        )
        book.file.save(
            f'image_{randint(0,2000)}.pdf',
            File(open('media/kotlin.pdf', 'rb')),
        )


def create_news_items():
    for i in range(0, 12):
        paragraphs = create_paragraph_model()
        news_item = NewsItemModel.objects.create(
            preview_text='Preview text preview text',
            title='Новость новость',
        )
        news_item.preview_image.save(
            f'image_{randint(0,2000)}.png',
            File(open('static/images/news_card_item.png', 'rb')),
        )
        for paragraph in paragraphs:
            news_item.content.add(paragraph)

        news_item.save()


def create_students():
    for i in range(0, 18):
        student = StudentModel.objects.create(
            full_name='Паников Паник Паникович',
            subtitle='Подзаголовок',
            email='as@gmail.com',
            description='''
                Описание Описание Описание Описание Описание Описание 
                Описание Описание Описание Описание Описание Описание 
                Описание Описание Описание Описание Описание Описание 
                Описание Описание Описание Описание Описание Описание 
                Описание Описание Описание Описание Описание Описание 
                Описание Описание Описание Описание Описание Описание 
            ''', # noqa
        )
        student.image.save(
            f'image_{randint(0,2000)}.png',
            File(open('static/images/student_card_img.png', 'rb')),
        )
        student.save()


def create_results():
    for i in range(0, 3):
        result = ResultModel.objects.create(
            full_name='ИВАНОВ ПАВЕЛ ДУРОВ',
            subtitle='Студент 3-го курса',
            email='sdklf@gmail.com',
            description='''
                Но укрепление и развитие внутренней структуры напрямую зависит от существующих финансовых и административных условий. Высокий уровень вовлечения представителей целевой аудитории является четким доказательством простого факта:
            ''' # noqa
        )
        result.image.save(
            f'image_{randint(0,2000)}.png',
            File(open('static/images/student_card_img.png', 'rb')),
        )
        result.save()


def create_practice():
    paragraphs = create_paragraph_model()
    course = CourseModel.objects.get(number=2)
    practice = PracticeModel(
        title='Course Project',
        subtitle='Subtitle of course project',
        course=course,
    )
    practice.image.save(
        f'image_{randint(0,2000)}.png',
        File(open('static/images/profile_photo.png', 'rb')),
    )
    practice.save()

    for paragraph in paragraphs:
        practice.content.add(paragraph)


def create_records():
    create_about_us_model()
    create_paragraph_model()
    create_course_model()
    create_course_projects()
    create_books()
    create_news_items()
    create_students()
    create_results()
    create_practice()
