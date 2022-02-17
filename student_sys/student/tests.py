from django.test import TestCase, Client

from .models import Student


# Create your tests here.

class StudengTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='nobody@the5fire.com',
            profession='程序员',
            qq='33333333',
            phone='2333333322222',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='yangsai',
            sex=1,
            email='32154332@qq.com',
            profession='程序员',
            qq='3333332222222',
            phone='3232432432',
        )
        # self.assertEqual(student.get_sex_display, '男', '性别字段内容跟展示不一致!')
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一致!')

    def test_filter(self):
        Student.objects.create(
            name='yangsai',
            sex=1,
            email='32154332@qq.com',
            profession='程序员',
            qq='3333332222222',
            phone='3232432432',
        )
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='3333@dd.com',
            qq='34543543',
            phone='454367657',
        )
        response = client.post('/', data)
        self.assertTrue(b'test_for_post' in response.content, "response content must contain 'test_for_post'")
