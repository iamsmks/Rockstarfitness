from django.db import models

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Membership(models.Model):
    payment= False

    def __str__(self):
        return self.name
    

class GExercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    video=models.URLField(blank=True)
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.name
    def get_link_html(self):
        if self.video:
            return '<a href="{}" target="_blank">{}</a>'.format(self.video, self.video)
        else:
            return '-'

    get_link_html.allow_tags = True
    get_link_html.short_description = 'video'

class HExercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    video=models.URLField(blank=True)
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.name
    
class Yoga(models.Model):
    name = models.CharField(max_length=100)
    Benefitss = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    video=models.URLField(blank=True)
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.name
    
class S_Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    video=models.URLField(blank=True)
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.name
    
class pt_Exercises(models.Model):
   
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200, null=True,) 
    def str(self):
        return self.name
       

class Contact(models.Model):
    def str(self):
        return self.name
    
class Membership(models.Model):
    def str(self):
        return self.name
 
 #class Checkout(models.Model):
    #fname=models.CharField(max_length=200, null=True,)
    #email=models.CharField(max_length=200, null=True,)
    #a3ddress=models.CharField(max_length=200, null=True,)
    #city= models.CharField(max_length=200, null=True,)
    #state=models.CharField(max_length=200, null=True,)
    #zip=models.BigIntegerField( null=True) 
    #cname=models.CharField(max_length=200, null=True,)
    #cnumber=models.BigIntegerField( null=True)
    #def str(self):
         #return self.name
 

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

    

