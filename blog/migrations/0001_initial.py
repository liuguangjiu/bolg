# Generated by Django 2.1rc1 on 2020-11-28 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('author', models.CharField(max_length=30, verbose_name='文章作者')),
                ('description', models.CharField(max_length=200, verbose_name='文章描述')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('thumb', models.URLField(default='https://ww2.sinaimg.cn/large/a15b4afegy1fil8yrpuejj212w0p5n09.jpg', verbose_name='特色图')),
                ('views', models.IntegerField(default=0, verbose_name='浏览量')),
                ('is_recommand', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('love', models.IntegerField(default=0, verbose_name='点赞数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'blog_article',
                'ordering': ['-date_publish'],
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='链接地址')),
                ('title', models.CharField(max_length=20, verbose_name='图片标题')),
                ('description', models.CharField(max_length=40, verbose_name='图片描述')),
                ('image', models.URLField(verbose_name='图片地址')),
                ('index', models.IntegerField(default=999, verbose_name='轮播图顺序（从小到大）')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'blog_carousel',
                'ordering': ['index', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='固定链接')),
                ('description', models.CharField(max_length=200, verbose_name='分类描述')),
                ('index', models.IntegerField(default=999, verbose_name='分类权重')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'blog_category',
                'ordering': ['index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='链接地址')),
                ('name', models.CharField(max_length=50, verbose_name='站点名称')),
                ('description', models.CharField(max_length=100, verbose_name='站点描述')),
                ('show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('index', models.IntegerField(default=99, verbose_name='排列顺序（从小到大）')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'db_table': 'blog_links',
                'ordering': ['index', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='站点标题')),
                ('subtitle', models.CharField(max_length=50, verbose_name='站点副标题')),
                ('keywords', models.CharField(max_length=300, verbose_name='站点关键词（最大长度300）')),
                ('description', models.CharField(max_length=150, verbose_name='站点描述（最大长度150）')),
                ('favicon', models.URLField(verbose_name='站点小图标地址')),
                ('logo', models.URLField(verbose_name='站点Logo地址')),
            ],
            options={
                'verbose_name': '全局设置',
                'verbose_name_plural': '全局设置',
                'db_table': 'blog_settings',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='标签名称')),
                ('index', models.IntegerField(default=999, verbose_name='标签权重')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'blog_tags',
                'ordering': ['index', 'id'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='article', to='blog.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='article', to='blog.Tag', verbose_name='文章标签'),
        ),
    ]
