# -*- encoding:utf-8 -*-

from django.db import models

#办学类型
class BASE_BXLX(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    layer = 3

#单位办别
class BASE_DWBB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#单位类别
class BASE_DWLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=50)
    layer = 1
    
#所在地城乡类型代码
class BASE_SZDCXLX(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=10)
    layer = 3
    
#所在地区经济属性代码
class BASE_SZDQJJSX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#学校办别代码
class BASE_XXBB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#学校变更代码表
class BASE_XXBG(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#学校单位层次代码
class BASE_XXDWCC(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#学校性质代码
class BASE_XXXZ(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=10)
    layer = 1
    
#安全教学形式代码
class BASE_AQJXXS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#毕业去向代码表
class BASE_BYQX(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=15)
    layer = 2
    
#处分名称代码
class BASE_CFMC(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#残疾人类型代码
class BASE_CJRLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1

#高考科目代码
class BASE_GKKM(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=5)
    layer = 1
    
#获奖类型代码
class BASE_HJLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#就读方式代码
class BASE_JDFS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#奖励方式代码
class BASE_JLFS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#家庭类别代码
class BASE_JTLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=15)
    layer = 1
    
#奖学金类型代码
class BASE_XJLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=40)
    layer = 1
    
#困难程度代码
class BASE_KNCD(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#困难原因代码
class BASE_KNYY(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#录取类别代码
class BASE_LQLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1

#入学方式代码表
class BASE_RXFS(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1

#体检项目类别代码
class BASE_TJXMLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#违纪类别代码
class BASE_WJLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    layer = 1
    
#学籍异动类别代码
class BASE_XJYDLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    layer = 1
    
#学籍异动原因代码
class BASE_XJYDYY(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    layer = 2
    
#学生变动代码
class BASE_XSBD(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=5)
    layer = 2

#学生当前状态代码
class BASE_XSDQZT(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#学生获奖类别代码
class BASE_XSHJLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#学生类别代码
class BASE_XSLB(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    layer = 3
    
#学生来源代码
class BASE_XSLY(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    layer = 3

#学生体质达标代码
class BASE_XSTZDB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#休退学原因代码
class BASE_XTXYY(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#严重不良行为代码
class BASE_YZBLXW(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=30)
    layer = 1
    
# 中小学学生来源代码
class BASE_ZXXXSLY(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#班额代码
class BASE_BE(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=30)
    layer = 1
    
#监考人类别代码
class BASE_JKRLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#教室类型代码
class BASE_JSLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#教学类型代码
class BASE_JXLX(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#教学用房性质代码
class BASE_JXYFXZ(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2

#考试方式代码
class BASE_KSFS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#考试形式代码
class BASE_KSXS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1

#考试性质代码
class BASE_KSXZ(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#年级代码
class BASE_NJ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
# 入学年龄代码
class BASE_RXNL(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#缺考舞弊代码
class BASE_QKWB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#授课方式代码
class BASE_SKFS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#少数民族双语教学模式代码
class BASE_SSMZSYJXMS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1

#学期代码
class BASE_XQ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#学制代码
class BASE_XZ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#幼儿班级类型代码
class BASE_YEBJLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1

#招生对象代码
class BASE_ZSDX(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    layer = 2

#中小学班级类型代码
class BASE_ZXXBJLX(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    layer = 2
    
#中小学编制类别代码
class BASE_ZXXBZLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#中小学课程代码
class BASE_ZXXKC(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#中小学课程等级代码
class BASE_ZXXKCDJ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#中小学实验类别代码
class BASE_ZXXSYLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#性别
class BASE_XB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=2)
    layer = 1
    
#岗位职业代码
class BASE_GWZY(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    layer = 2
    
# 教师获奖类别代码
class BASE_JSHJLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
# 教职工当前状态代码
class BASE_JZGDQZT(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#教职工类别代码
class BASE_JZGLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    layer = 2
    
#教职工来源代码
class BASE_JZGLY(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    layer = 2
    
#离岗原因代码
class BASE_LGYY(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#离校离职原因代码
class BASE_LXLZYY(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#聘任情况代码
class BASE_PRQK(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#聘用性质代码
class BASE_PYXZ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#任课角色代码
class BASE_RKJS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#任课学段代码
class BASE_RKXD(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#职务类别代码
class BASE_ZWLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#港澳台侨外代码
class BASE_GATQW(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#级别代码
class BASE_JB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#奖励等级代码
class BASE_JLDJ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#普通话水平等级代码
class BASE_PTHSPDJ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#是否标志代码
class BASE_SFBZ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=2)
    layer = 1
    
#身份证件类型代码
class BASE_SFZJLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#社会单位性质代码
class BASE_SHDWXZ(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#血型代码
class BASE_XX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
# 出版社级别代码
class BASE_CBSJB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#成果获奖类别
class BASE_CGHJLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1

#成果类型代码
class BASE_CGLX(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    layer = 2
    
#鉴定结论代码
class BASE_JDJL(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=10)
    layer = 1
    
# 计划完成情况代码
class BASE_JHWCQK(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#角色代码
class BASE_JS(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    layer = 2
    
#刊物级别代码
class BASE_KWJB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#论文报告形式代码
class BASE_LWBGXS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#论著类别代码
class BASE_LZLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=10)
    layer = 2
    
#社会经济效益代码
class BASE_SHJJXY(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#受让方类型代码
class BASE_SRFLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#完成形式代码
class BASE_WCXS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#学科门类(科技)代码
class BASE_XKMLKJ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1

#项目经费来源代码
class BASE_XMJFLY(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#项目类型代码
class BASE_XMLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1

#项目来源代码
class BASE_XMLY(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 20
    
#项目执行状态代码
class BASE_XMZXZT(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
#学术会议等级代码
class BASE_XSHYDJ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#学术交流类型代码
class BASE_XSJLLX(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#学术团体级别代码
class BASE_XSTTJB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#协作单位类型代码
class BASE_XZDWLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#专利法律状态代码
class BASE_ZLFLZT(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#专利类型代码
class BASE_ZLLX(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#专利批准形式代码
class BASE_ZLPZXS(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#考核类别代码
class BASE_GBTKHLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#考核结论代码
class BASE_GBTKHJL(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    layer = 1
    
#语种类别
class BASE_GBYZLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=10)
    layer = 1
    
#编制类别
class BASE_GBBZLB(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
#岗位类别
class BASE_GBGWLB(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#家庭关系
class BASE_GBJTGX(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#婚姻状况
class BASE_GBHYZK(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1
    
#学历代码
class BASE_GBXLDM(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 2
    
#政治面貌
class BASE_GBZZMM(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    layer = 1

# 行政区划
class BASE_GBXZQH(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=5)
    layer = 3
    
# 民族
class BASE_GBMZ(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=5)
    layer = 3
    
#健康状况
class BASE_GBJKZK(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
# 宗教信仰
class BASE_GBZJXY(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
# 户口性质
class BASE_GBHKXZ(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=10)
    layer = 1
    
# 学位代码
class BASE_GBXWDM(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    layer = 2
    
# 专业技术职务
class BASE_GBZYJSZW(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    layer = 2
    
# 职务级别码
class BASE_GBZWJBM(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    layer = 2
    
# 学生注册状况
class BASE_ZCZK(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
# 教育培训结果
class BASE_GBJYPXJG(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
# 刊物装订
class BASE_KWZD(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=5)
    layer = 1
    
    