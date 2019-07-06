from django.db import models

class Account(models.Model):
    global_id = models.BigIntegerField(verbose_name = 'Глобальный идентификатор')
    name_full = models.CharField(max_length = 100, verbose_name = 'Фирменное наименование юридического лица')
    name_short = models.CharField(max_length = 100, verbose_name = 'Сокращенное наименование')
    name_employee = models.CharField(max_length = 100, verbose_name = 'ФИО руководителя')
    inn = models.CharField(max_length = 100, verbose_name = 'Идентификационный номер налогоплательщика')
    ogrn = models.CharField(max_length = 100, verbose_name = 'ОГРН')
    legal_address = models.CharField(max_length = 100, verbose_name = 'Адрес юридического лица')
    actual_address =  models.CharField(max_length = 100, verbose_name = 'Адрес фактического местонахождения органов управления')
    phone = models.CharField(max_length = 100, verbose_name = 'Контактные телефоны')
    email = models.EmailField(verbose_name = 'Email')

    def __str__(self):
        return self.name_full

    class Meta:
        verbose_name = 'Управляющая организация'
        verbose_name_plural = 'Управляющие организации'

class Service(models.Model):
    tsj_id = models.BigIntegerField(verbose_name = 'Идентификатор ТСЖ', default=-1)
    house_id = models.IntegerField(verbose_name='Идентификатор дома', blank = True)
    address = models.CharField(max_length = 50, verbose_name = 'Адрес дома')
    breakdown = models.CharField(max_length = 50, verbose_name = 'Категория поломки')
    name = models.CharField(max_length = 100, verbose_name = "Услуга", default = 'Тестовая услуга')
    challenge_accepted = models.DateField(verbose_name='Дата принятия вызова')
    challenge_done = models.DateField(verbose_name='Дата выполнения', blank = True, null = True)
    man_company = models.ForeignKey(Account, on_delete = models.CASCADE, related_name='challenges', null = True)
    status = models.CharField(max_length = 20, verbose_name = 'Статус выполнения', default = 'done')

    class Meta:
        verbose_name = 'Заявка на выполение работы'
        verbose_name_plural = 'Заявки на выполнение работы'

