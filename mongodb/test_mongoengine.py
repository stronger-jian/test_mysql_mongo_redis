#ODM:Object Document Mapping,本质也属于一种ORM,
from mongoengine import *
#connect,StringField,IntField,FloatField,ListField,EmbeddedDocument,EmbeddedDocumentField,Document,DynamicDocument


connect('students')


class Grade(EmbeddedDocument):
    name=StringField(required=True)
    score=FloatField(required=True)
	

SEX_CHOICES=(('male','男'),('femaile','女'))


class Student(DynamicDocument):
    name = StringField(required=True, max_length=30)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grade=FloatField()
    address=StringField()
    grades=ListField(EmbeddedDocumentField(Grade))
    #remark=StringField()
    
    #者可以指定数据保存的集合
    meta={
        'collection':'students',
        'ordering':['id']
    }
       
class TestMongoEngine(object):
    ''' 添加一条数据到数据库 '''
    def add_one(self):
        yuwen= Grade(
            name='语文',
            score=90
        )
        shuxue=Grade(
            name='数学',
            score=100
        )
        stu_obj=Student(
            name='李四5',
            age=19,
            sex='male',
            grades=[yuwen,shuxue]
        )
        stu_obj.remark='remark'
        stu_obj.save()
        return stu_obj
        
    def get_one(self):
        ''' 查询一条数据 '''
        return Student.objects.first()
        
    def get_more(self):
        ''' 查询多条数据 '''
        return Student.objects.all().first()
        
    def get_by_oid(self,oid):
        ''' 根据对象id 查询数据 '''
        return Student.objects.filter(id=oid).first()
        
    def update(self):
        ''' 修改数据 '''
        #男生年龄 加十岁
        # return Student.objects.filter(sex='male').update(inc__age=10)
        #修改一条数据
        return Student.objects.filter(sex='male').update_one(inc__age=100)
        
    def delete(self):
        ''' 删除数据 '''
        #删除一条数据
        # return Student.objects.filter(sex='male').first().delete()
        #删除多条数据
        return Student.objects.filter(sex='male').delete()
    
def main():
    obj=TestMongoEngine()
    # rest=obj.add_one()
    # print(rest.pk)
    
    # rest=obj.get_one()
    # print(rest.name)
    
    # rows=obj.get_more()
    #for row in rows:
    # print(rows.name)
        
    # rest=obj.get_by_oid('5b7624f4f559ca04ec3c4e23')
    # if rest:
        # print(rest.id)
        # print(rest.name)
    
    #成功后 返回的是 修改的数据数
    # rest=obj.update()
    # print(rest)
    
    rest=obj.delete()
    print(rest)
    
if __name__ == '__main__':
        main()