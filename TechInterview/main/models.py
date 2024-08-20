from django.db import models


class Profession(models.Model):
    class Meta:
        db_table = 'profession'

    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    class Meta:
        db_table = 'tag'

    title = models.CharField(max_length=50)
    professions = models.ManyToManyField(Profession, related_name='tags')

    def __str__(self):
        return self.title


class Answer(models.Model):
    class Meta:
        db_table = 'answer'

    text = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.text

class Question(models.Model):
    class Meta:
        db_table = 'question'

    title = models.CharField(max_length=500)
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    chance = models.PositiveIntegerField()
    answer = models.OneToOneField(Answer, on_delete=models.PROTECT)
    profession = models.ForeignKey(to=Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Interview(models.Model):
    class Meta:
        db_table = 'interview'

    title = models.CharField(max_length=500)
    url = models.URLField()
    profession = models.ForeignKey(to=Profession, on_delete=models.CASCADE)
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Skill(models.Model):
    class Meta:
        db_table = 'skill'

    title = models.CharField(max_length=50)
    number_of_mentions = models.PositiveIntegerField()
    profession = models.ForeignKey(to=Profession, on_delete=models.CASCADE)