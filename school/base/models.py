# -*- encoding:utf-8 -*-
from django.db import models
from common import models as common_models

# Create your models here.
class Zhuguanbumen(models.Model):
    pass

# 学校
class Xuexiao(models.Model):
    xxdm = models.CharField(unique=True,null=False,max_length=10,verbose_name=u"学校代码")
    xxmc = models.CharField(unique=True,null=False,max_length=255,verbose_name=u"学校名称")
    xxywmc = models.CharField(blank=True,max_length=255,verbose_name=u"学校英文名称")
    xxdz = models.CharField(max_length=255,verbose_name=u"学校地址")
    xxyzbm = models.CharField(max_length=6,verbose_name=u"邮政编码")
    xzqhm = models.ForeignKey(common_models.BASE_GBXZQH,verbose_name=u"行政区划")
    jxny = models.DateField(verbose_name=u"建校年月")
    xqr = models.IntegerField(verbose_name=u"校庆日")
    xxbxlxm = models.ForeignKey(common_models.BASE_BXLX,verbose_name=u"学校办学类型")
    xxzgbmm = models.ForeignKey(Zhuguanbumen,null=True,verbose_name=u"学校主管部门")
    fddbrh = models.CharField(blank=True,max_length=20,verbose_name=u"法定代表人号")
    frzsh = models.CharField(max_length=20,verbose_name=u"法人证书号")
    xzgh = models.CharField(blank=True,max_length=20,verbose_name=u"校长工号")
    xzxm = models.CharField(max_length=50,verbose_name=u"校长姓名")
    dwfzrh = models.CharField(max_length=20,blank=True,verbose_name=u"党委负责人号")
    zzjgm = models.CharField(blank=True,max_length=20,verbose_name=u"组织机构码")
    lxdh = models.CharField(max_length=30,verbose_name=u"联系电话")
    czdh = models.CharField(max_length=30,verbose_name=u"传真电话")
    dzyx = models.EmailField(verbose_name=u"电子邮箱")
    zydz = models.URLField(verbose_name=u"主页地址")
    lsyg = models.TextField(blank=True,verbose_name=u"历史沿革")
    xxbbm = models.ForeignKey(common_models.BASE_XXBB,verbose_name=u"学校办别")
    sszgdwm = models.CharField(max_length=6,blank=True,verbose_name=u"所属主管单位")
    szdcxlxm = models.ForeignKey(common_models.BASE_SZDCXLX,verbose_name=u"所在地城乡类型")
    szdjjsxm = models.ForeignKey(common_models.BASE_SZDQJJSX,verbose_name=u"所在地经济属性")
    szdmzsx = models.BooleanField(verbose_name=u"所在地民族属性")
    xxxz = models.IntegerField(verbose_name=u"小学学制")
    xxrxnl = models.IntegerField(verbose_name=u"小学入学年龄")
    czxz = models.IntegerField(verbose_name=u"初中学制")
    czrxnl = models.IntegerField(verbose_name=u"初中入学年龄")
    gzxz = models.IntegerField(verbose_name=u"高中学制")
    zjxyy = models.ForeignKey(common_models.BASE_GBYZLB,verbose_name=u"主教学语言")
    fjxyy = models.ForeignKey(common_models.BASE_GBYZLB,verbose_name=u"辅教学语言",related_name="xuexiao_fjxyy_to_base_gbyzlb")
    zsbj = models.CharField(max_length=30,verbose_name=u"招生半径")
    
class Nianji(models.Model):
    nj = models.ForeignKey(common_models.BASE_NJ,verbose_name=u"年级")
    njmc = models.CharField(max_length=30,verbose_name=u"年级名称")
    xuexiao = models.ForeignKey(Xuexiao)

# 班级    
class Banji(models.Model):
    bh = models.CharField(max_length=15,verbose_name=u"班级号")
    bj = models.CharField(max_length=30,verbose_name=u"班级名称")
    jbny = models.DateField(verbose_name=u"建班日期")
    bzrgh = models.ForeignKey("Jiaozhigong",verbose_name=u"班主任")
    bzxh = models.ForeignKey("Xuesheng",verbose_name=u"班长")
    bjrych = models.CharField(max_length=40,blank=True,verbose_name=u"班级荣誉称号")
    xz = models.IntegerField(verbose_name=u"学制")
    bjlxm = models.ForeignKey(common_models.BASE_ZXXBJLX,null=True,verbose_name=u"班级类型")
    wllx = models.NullBooleanField(verbose_name=u"文理类型") #null＝小学、初中 True＝高中文 False＝高中理
    byrq = models.DateField(verbose_name=u"毕业日期")
    sfssmzsyjxb = models.BooleanField(verbose_name=u"少数民族双语教学班")
    syjxmsm = models.ForeignKey(common_models.BASE_SSMZSYJXMS,verbose_name=u"双语教学模式",null=True)
    xuexiao = models.ForeignKey(Xuexiao)

# 学生
class Xuesheng(models.Model):
    xh = models.IntegerField(verbose_name=u"学号")
    xm = models.CharField(max_length=30,verbose_name=u"姓名")
    ywxm = models.CharField(max_length=30,blank=True,verbose_name = u"英文姓名")
    xmpy = models.CharField(max_length=30,blank=True,verbose_name = u"姓名拼音")
    cym = models.CharField(max_length=30,blank=True,verbose_name=u"曾用名")
    xbm = models.ForeignKey(common_models.BASE_XB,verbose_name=u"性别")
    csrq = models.DateField(verbose_name=u"出生日期")
    csdm = models.ForeignKey(common_models.BASE_GBXZQH,verbose_name=u"出生地",related_name=u"xuesheng_csdm_to_base_gbxzqh")
    jg = models.ForeignKey(common_models.BASE_GBXZQH,verbose_name=u"籍贯",null=True,related_name=u"xuesheng_jg_to_base_gbxzqh")
    mzm = models.ForeignKey(common_models.BASE_GBMZ,verbose_name=u"民族",blank=True)
    gjdqm = models.CharField(max_length=20,blank=True,verbose_name=u"国籍地区码")
    sfzjlx = models.ForeignKey(common_models.BASE_SFZJLX,null=True,verbose_name=u"身体证件类型")
    sfzjh = models.CharField(max_length=30,blank=True,verbose_name=u"身份证件号")
    gatqwm = models.ForeignKey(common_models.BASE_GATQW,null=True,verbose_name=u"港澳台侨外")
    zzmmm = models.ForeignKey(common_models.BASE_GBZZMM,verbose_name=u"政治面貌")
    jkzkm = models.ForeignKey(common_models.BASE_GBJKZK,verbose_name=u"健康状况")
    xyzjm = models.ForeignKey(common_models.BASE_GBZJXY,null=True,verbose_name=u"宗教信仰")
    xxm = models.ForeignKey(common_models.BASE_XX,null=True,verbose_name=u"血型")
    #zp = models.ImageField()
    sfzjyxq = models.IntegerField(verbose_name=u"身份证件有效期")
    dsznbz = models.BooleanField(default=True,verbose_name=u"独生子女标志")
    rxny = models.DateField(verbose_name=u"入学年月")
    nj = models.ForeignKey(Nianji,verbose_name=u"年级",null=True)
    bh = models.ForeignKey(Banji,verbose_name=u"班级",null=True)
    xslbm = models.ForeignKey(common_models.BASE_XSLB,verbose_name=u"学生类别")
    xzz = models.CharField(max_length=255,blank=True,verbose_name=u"现住址")
    hkszd = models.CharField(max_length=255,blank=True,verbose_name=u"户口所在地")
    hkxzm = models.ForeignKey(common_models.BASE_GBHKXZ,null=True,verbose_name=u"户口性质")
    sfldrk = models.BooleanField(default=False,verbose_name=u"流动人口")
    tc = models.TextField(verbose_name=u"特长",blank=True)
    lxdh = models.CharField(max_length=30,verbose_name=u"联系电话",blank=True)
    txdz = models.CharField(max_length=255,blank=True,verbose_name=u"通信地址")
    yzbm = models.CharField(max_length=5,blank=True,verbose_name=u"邮政编码")
    dzxx = models.EmailField(verbose_name=u"电子信箱")
    zydz = models.URLField(verbose_name=u"主页地址")
    xjh = models.CharField(max_length=20,verbose_name=u"学籍号")
    xuexiao = models.ForeignKey(Xuexiao,verbose_name=u"学校")

# 学生学习简介    
class Xueshengxuexijianli(models.Model):
    xuesheng = models.ForeignKey(Xuesheng,verbose_name=u"学生")
    xxqsrq = models.DateField(verbose_name=u"学习起始日期")
    xxzzrq = models.DateField(verbose_name=u"学习终止日期")
    xxdw = models.CharField(max_length=255,verbose_name=u"学习单位")
    xxnr = models.CharField(max_length=255,blank=True,verbose_name=u"学习内容")
    sxzymc = models.CharField(max_length=255,blank=True,verbose_name=u"所学专业名称")
    shxwm = models.ForeignKey(common_models.BASE_GBXWDM,null=True,verbose_name=u"所获学位")
    xxzmr = models.CharField(max_length=30,blank=True,verbose_name=u"学习证明人")
    xxjlbz = models.TextField(blank=True,verbose_name=u"学习简历备注")
    
# 家庭成员
class Jiantingchengyuan(models.Model):
    xuesheng = models.ForeignKey(Xuesheng,verbose_name=u"学生")
    gxm = models.ForeignKey(common_models.BASE_GBJTGX,verbose_name=u"关系")
    cyxm = models.CharField(max_length=30,verbose_name=u"成员姓名")
    csny = models.DateField(null=True,verbose_name=u"出生年月")
    mzm = models.ForeignKey(common_models.BASE_GBMZ,null=True,verbose_name=u"民族")
    #gjdq = models.CharField(max_length=10,verbose=u"国籍/地区")
    jkzkm = models.ForeignKey(common_models.BASE_GBJKZK,null=True,verbose_name=u"健康状况")
    cygzdw = models.CharField(max_length=255,blank=True,verbose_name=u"成员工作单位")
    #cym = models.ForeignKey(verbose_name=u"从业状况")
    zyjszwm = models.ForeignKey(common_models.BASE_GBZYJSZW,null=True,verbose_name=u"专业技术职务") 
    zwjbm = models.ForeignKey(common_models.BASE_GBZWJBM,null=True,verbose_name=u"职务级别")
    dh = models.CharField(max_length=30,blank=True,verbose_name=u"电话")
    dzxx = models.EmailField(verbose_name=u"电子信息")
    sfjhr = models.BooleanField(default=True,verbose_name=u"是否监护人")
    xbm = models.ForeignKey(common_models.BASE_XB,verbose_name=u"性别")
    xlm = models.ForeignKey(common_models.BASE_GBXLDM,verbose_name=u"学历")
    lxdz = models.CharField(max_length=255,blank=True,verbose_name=u"联系地址")
    sjhm = models.CharField(max_length=30,blank=True,verbose_name=u"手机号码")
    
# 学生注册子类
class Xueshengzhuce(models.Model):
    xuesheng = models.ForeignKey(Xuesheng,verbose_name=u"姓名")
    zczk = models.ForeignKey(common_models.BASE_ZCZK,verbose_name=u"注册状况")
    zcbh = models.ForeignKey(Banji,verbose_name=u"班级")
    yqzwzcrq = models.DateField(verbose_name=u"最晚注册日期",null=True)
    sjzcrq = models.DateField(verbose_name=u"实际注册日期",null=True)
    waszcyy = models.CharField(max_length=255,blank=True,verbose_name=u"未按时注册原因")
    bzcrq = models.DateField(null=True,verbose_name=u"补注册日期")
    

#学籍异动
class Xuejiyidong(models.Model):
    xuesheng=models.ForeignKey(Xuesheng,verbose_name=u"学生")
    ydlbm = models.ForeignKey(common_models.BASE_XJYDLB,verbose_name=u"异动类别")
    ydrq = models.ForeignKey(common_models.BASE_XJYDYY,verbose_name=u"异动原因")
    sprq = models.DateField(verbose_name=u"审批日期")
    spwh = models.CharField(max_length=24,blank=True,verbose_name=u"审批文号")
    ydlyxxm = models.CharField(max_length=20,blank=True,verbose_name=u"异动来源学校码")
    ydqxxxm = models.CharField(max_length=20,blank=True,verbose_name=u"异动支向学校码")
    ydsm = models.TextField(blank=True,verbose_name=u"异动说明")

#学籍成绩 学生日常考试通过计入学籍操作存入该表   
class Xuejichengji(models.Model):
    xuesheng = models.ForeignKey(Xuesheng,verbose_name=u"学生")
    xuexiao = models.ForeignKey(Xuexiao)
    nj = models.ForeignKey(Nianji,verbose_name=u"年级")
    xn = models.CharField(max_length=8,verbose_name=u"学年")
    xqm = models.ForeignKey(common_models.BASE_XQ,verbose_name=u"学期")
    ksrq = models.DateField(verbose_name=u"考试日期")
    kch = models.ForeignKey(common_models.BASE_ZXXKC,verbose_name=u"课程")
    pscj = models.FloatField(verbose_name=u"平时成绩",null=True)
    ksfs = models.ForeignKey(common_models.BASE_KSFS,verbose_name=u"考试方式")
    ksxz = models.ForeignKey(common_models.BASE_KSXZ,verbose_name=u"考试性质")
    ksxs = models.ForeignKey(common_models.BASE_KSXS,verbose_name=u"考试形式")
    fslkscj = models.IntegerField(verbose_name=u"分数类成绩",null=True)
    djlkscj = models.CharField(max_length=10,blank=True,verbose_name=u"等级类考试成绩")
    kccj = models.IntegerField(verbose_name=u"课程成绩")
    kcdjcjm = models.CharField(max_length=10,blank=True,verbose_name=u"课程等级成绩码")
    rkjsgh = models.ForeignKey("Jiaozhigong",verbose_name=u"任课教师",related_name="Xuejichengji_rkjsgh_to_jiaozhigong")
    cjlrrh = models.ForeignKey("Jiaozhigong",verbose_name=u"录入教师",related_name="Xuejichengji_cjlrrh_to_jiaozhigong")
    cjlrrq = models.DateField(verbose_name=u"成绩录入日期")
    cjlrsj = models.TimeField(verbose_name=u"成绩录入时间")
    
# 奖励
class Jiangli(models.Model):
    xuesheng = models.ForeignKey(Xuesheng,verbose_name=u"学生")
    jlmc = models.CharField(max_length=60,verbose_name=u"奖励名称")
    jljbm = models.ForeignKey(common_models.BASE_JB,verbose_name=u"级别")
    jldjm = models.ForeignKey(common_models.BASE_JLDJ,verbose_name=u"等级")
    jllbm = models.ForeignKey(common_models.BASE_XSHJLB,verbose_name=u"获奖类别")
    jlyy = models.CharField(max_length=100,blank=True,verbose_name=u"奖励原因")
    jlje = models.IntegerField(verbose_name=u"奖励金额",null=True)
    jlwh = models.CharField(max_length=24,blank=True,verbose_name=u"奖励文号")
    xuexiao = models.ForeignKey(Xuexiao,verbose_name=u"学校")
    jlxnd = models.CharField(max_length=8,verbose_name=u"奖励学年度")
    bjdw = models.CharField(max_length=255,verbose_name=u"授奖单位")
    jllxm = models.ForeignKey(common_models.BASE_HJLX,verbose_name=u"奖励类型",null=True)
    jlfsm = models.ForeignKey(common_models.BASE_JLFS,verbose_name=u"奖励方式",null=True)

#惩处数据
class Chengchu(models.Model):
    xuesheng=models.ForeignKey(Xuesheng,verbose_name=u"学生")
    xuexiao = models.ForeignKey(Xuexiao,verbose_name=u"学校")
    wjrq = models.DateField(verbose_name=u"违纪日期")
    wjjk = models.CharField(max_length=100,blank=True,verbose_name=u"违纪简况")
    wjlbm = models.ForeignKey(common_models.BASE_WJLB,verbose_name=u"违纪类别")
    cfmcm = models.ForeignKey(common_models.BASE_CFMC,verbose_name=u"处分名称")
    cfyy = models.CharField(max_length=100,blank=True,verbose_name=u"处分原因")
    cfwh = models.CharField(max_length=24,blank=True,verbose_name=u"处分文号")
    cfcxrq = models.DateField(null=True,verbose_name=u"处分撤销日期")
    cfcxwh = models.CharField(max_length=24,blank=True,verbose_name=u"处分撤销文号")
    cfrq = models.DateField(verbose_name=u"处分日期",null=True)

#结束学业数据
class Jieshuxueye(models.Model):
    xuesheng = models.ForeignKey(Xuesheng,verbose_name=u"学生")
    xuexiao = models.ForeignKey(Xuexiao,verbose_name=u"学校")
    jsxyny = models.DateField(verbose_name=u"结束学业年月")
    jsxym = models.ForeignKey(common_models.BASE_GBJYPXJG,verbose_name=u"教育教训结果")
    jsxyyysm = models.CharField(max_length=100,blank=True,verbose_name=u"结果学业原因说明")
    

#毕业数据
class Biye(models.Model):
    xuesheng = models.ForeignKey(Xuesheng,verbose_name=u"学生")
    xuexiao = models.ForeignKey(Xuexiao,verbose_name=u"学校")
    byny = models.DateField(verbose_name=u"毕业年月")
    bypy = models.TextField(blank=True,verbose_name=u"毕业评语")
    byqxm = models.ForeignKey(common_models.BASE_BYQX,verbose_name=u"毕业去向")
    byzsh = models.CharField(max_length=20,blank=True,verbose_name=u"毕业证书号")
    ffrq = models.DateField(null=True,verbose_name=u"发放日期")
    sfylq = models.BooleanField(verbose_name=u"领取")
    
class Jiaozhigong(models.Model):
    xuexiao = models.ForeignKey(Xuexiao,verbose_name=u"学校")
    gh = models.CharField(max_length=20,verbose_name=u"工号")
    xm = models.CharField(max_length=50,verbose_name=u"姓名")
    ywxm = models.CharField(max_length=50,blank=True,verbose_name=u"英文姓名")
    xmpy = models.CharField(max_length=50,blank=True,verbose_name=u"姓名拼音")
    cym = models.CharField(max_length=50,blank=True,verbose_name=u"曾用名")
    xbm = models.ForeignKey(common_models.BASE_XB,verbose_name=u"性别")
    csrq = models.DateField(verbose_name=u"出生日期")
    csdm = models.ForeignKey(common_models.BASE_GBXZQH,verbose_name=u"出生地",related_name="Jiaozhigong_csdm_to_base_gbxzqh")
    jg = models.ForeignKey(common_models.BASE_GBXZQH,verbose_name=u"籍贯",related_name="Jiaozhigong_jg_to_base_gbxzqh")
    gjdqm = models.CharField(blank=True,max_length=100,verbose_name=u"国籍/地区码")
    gjdqm = models.CharField(max_length=20,blank=True,verbose_name=u"国籍地区码")
    sfzjlx = models.ForeignKey(common_models.BASE_SFZJLX,null=True,verbose_name=u"身体证件类型")
    sfzjh = models.CharField(max_length=30,blank=True,verbose_name=u"身份证件号")
    hyzkm = models.ForeignKey(common_models.BASE_GBHYZK,null=True,verbose_name=u"婚姻状况")
    gatqwm = models.ForeignKey(common_models.BASE_GATQW,null=True,verbose_name=u"港澳台侨外")
    zzmmm = models.ForeignKey(common_models.BASE_GBZZMM,verbose_name=u"政治面貌")
    jkzkm = models.ForeignKey(common_models.BASE_GBJKZK,verbose_name=u"健康状况")
    xyzjm = models.ForeignKey(common_models.BASE_GBZJXY,null=True,verbose_name=u"宗教信仰")
    xxm = models.ForeignKey(common_models.BASE_XX,null=True,verbose_name=u"血型")
    #zp = models.ImageField()
    sfzjyxq = models.IntegerField(verbose_name=u"身份证件有效期")
    jgh = models.CharField(max_length=20,blank=True,verbose_name=u"机构号")
    jtzz =  models.CharField(max_length=255,blank=True,verbose_name=u"家庭住址")
    xzz =  models.CharField(max_length=255,blank=True,verbose_name=u"现住址")
    hkszd = models.CharField(max_length=255,blank=True,verbose_name=u"户口所在地")
    hkxzm = models.ForeignKey(common_models.BASE_GBHKXZ,null=True,verbose_name=u"户口性质")
    xlm = models.ForeignKey(common_models.BASE_GBXLDM,verbose_name=u"学历")
    gzny = models.DateField(null=True,verbose_name=u"工作年月")
    lxny = models.DateField(null=True,verbose_name=u"来校年月")
    cjny = models.DateField(null=True,verbose_name=u"从教年月")
    bzlbm = models.ForeignKey(common_models.BASE_ZXXBZLB,verbose_name=u"编制类别")
    dabh = models.CharField(max_length=25,blank=True,verbose_name=u"档案编号")
    dawb = models.TextField(blank=True,verbose_name=u"档案文本")
    lxdh = models.CharField(max_length=30,verbose_name=u"联系电话",blank=True)
    txdz = models.CharField(max_length=255,blank=True,verbose_name=u"通信地址")
    yzbm = models.CharField(max_length=5,blank=True,verbose_name=u"邮政编码")
    dzxx = models.EmailField(verbose_name=u"电子信箱")
    zydz = models.URLField(verbose_name=u"主页地址")
    tc = models.TextField(blank=True,verbose_name=u"特长")
    gwzym = models.ForeignKey(common_models.BASE_GWZY,null=True,verbose_name=u"岗位职业码")
    zyrkxd = models.ForeignKey(common_models.BASE_RKXD,null=True,verbose_name=u"主要任课学段")
    jzgdqzt = models.ForeignKey(common_models.BASE_JZGDQZT,verbose_name=u"教职工当前状态")
    
# 课程数据
class Kecheng(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    kch = models.CharField(max_length=10,verbose_name=u"课程号")
    kcmc = models.CharField(max_length=20,verbose_name=u"课程名称")
    kcm = models.ForeignKey(common_models.BASE_ZXXKC,verbose_name=u"课程码")
    kcdjm = models.ForeignKey(common_models.BASE_ZXXKCDJ,verbose_name=u"中小学课程等级")
    kcbm = models.CharField(max_length=60,blank=True,verbose_name=u"课程别名")
    kcjj = models.TextField(blank=True,verbose_name=u"课程简介")
    kcyq = models.TextField(blank=True,verbose_name=u"课程要求")
    zxs = models.IntegerField(verbose_name=u"总学时")
    zhxs = models.IntegerField(verbose_name=u"周学时")
    zxxs = models.IntegerField(verbose_name=u"自学学时")
    skfsm = models.ForeignKey(common_models.BASE_SKFS,null=True,verbose_name=u"授课方式")
    jcbm = models.ForeignKey("Jiaocai",null=True,verbose_name=u"教材编码")
    cksm = models.TextField(blank=True,verbose_name=u"参考书目")
    
# 教材数据类
class Jiaocai(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    jcbm = models.CharField(max_length=24,verbose_name=u"教材编码")
    jcmc = models.CharField(max_length=255,verbose_name=u"教材名称")
    isbn = models.CharField(max_length=20,blank=True,verbose_name=u"教材名称")
    zz = models.CharField(max_length=255,verbose_name=u"作者")
    bb = models.CharField(max_length=20,verbose_name=u"版别")
    yc = models.CharField(max_length=10,blank=True,verbose_name=u"印次")
    dj = models.FloatField(verbose_name=u"定价")
    cbs = models.CharField(max_length=255,verbose_name=u"出版社")
    fxbh = models.CharField(max_length=25,blank=True,verbose_name=u"发行编号")
    cbrq = models.DateField(null=True,verbose_name=u"出版日期")
    zd = models.ForeignKey(common_models.BASE_KWZD,null=True,verbose_name=u"装订")
    kb = models.CharField(max_length=20,blank=True,verbose_name=u"开本")
    zs = models.IntegerField(verbose_name=u"字数",default=0)
    nrjj = models.TextField(blank=True,verbose_name=u"内容简介")

# 教学计划
class Jiaoxuejihua(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    kch = models.ForeignKey(Kecheng,verbose_name=u"课程号")
    sknj = models.ForeignKey(Nianji,verbose_name=u"授课年级")
    skxn = models.CharField(max_length=8,verbose_name=u"授课学年")
    skxqm = models.ForeignKey(common_models.BASE_XQ,verbose_name=u"授课学期")
    ksfsm = models.ForeignKey(common_models.BASE_KSFS,verbose_name=u"考试方式")
    
# 排课数据
class Paike(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    kch = models.ForeignKey(Kecheng,verbose_name=u"课程")
    skjsgh = models.ForeignKey(Jiaozhigong,verbose_name=u"授课教师")
    skbj = models.ForeignKey(Banji,verbose_name=u"授课班级")
    skrq = models.IntegerField(verbose_name=u"授课星期")
    skjs = models.IntegerField(verbose_name=u"节次")

# 考试信息数据类
class Kaoshi(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    ksmc = models.CharField(max_length=100,verbose_name=u"考试名称")
    ksrs = models.IntegerField(verbose_name=u"考试人数")
    ksfs = models.ForeignKey(common_models.BASE_KSFS,verbose_name=u"考试方式")
    ksxs = models.ForeignKey(common_models.BASE_KSXS,verbose_name=u"考试形式")
    ksxz = models.ForeignKey(common_models.BASE_KSXZ,verbose_name=u"考试性质")    
    sycks = models.ForeignKey("self",null=True,verbose_name=u"上次考试")
    
    
# 考试科目
class Kaoshikemu(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    kaoshi = models.ForeignKey(Kaoshi)
    kch = models.ForeignKey(Kecheng,verbose_name=u"课程号")
    ksrq = models.DateField(verbose_name=u"考试日期",null=True)
    kskssj = models.TimeField(verbose_name=u"考试开始时间",null=True)
    ksjssj = models.TimeField(verbose_name=u"考试结束时间",null=True)
    zf = models.IntegerField(verbose_name=u"总分")
    jg = models.IntegerField(verbose_name=u"及格分数")
    yx = models.IntegerField(verbose_name=u"优秀分数")
    cjlrrq = models.DateField(verbose_name=u"成绩录入日期",null=True)
    cjlrsj = models.TimeField(verbose_name=u"成绩录入时间",null=True)
    cjlrrh = models.ForeignKey(Jiaozhigong,null=True,verbose_name=u"录入教师",related_name="kaoshikemu_cjlrrh_to_jiaozhigong")
   
# 考场数据表
class Kaoshikaochang(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    kaoshi = models.ForeignKey(Kaoshi)
    kcmc = models.CharField(max_length=100,verbose_name=u"考场名称")
    kcrs = models.IntegerField(verbose_name=u"考场人数")
    
#考生表
class Kaosheng(models.Model):
    xuexiao = models.ForeignKey(Xuexiao)
    kaoshi = models.ForeignKey(Kaoshi)
    kaochang = models.ForeignKey(Kaoshikaochang,verbose_name=u"考场")
    kaohao = models.IntegerField(verbose_name=u"考号")
    kaosheng = models.ForeignKey(Xuesheng)
    kch = models.ForeignKey(Kecheng,verbose_name=u"课程")    
    pscj = models.FloatField(verbose_name=u"平时成绩",null=True)
    fslkscj = models.IntegerField(verbose_name=u"分数类成绩",null=True)
    djlkscj = models.CharField(max_length=10,blank=True,verbose_name=u"等级类考试成绩")
    kccj = models.IntegerField(verbose_name=u"课程成绩")
    
    