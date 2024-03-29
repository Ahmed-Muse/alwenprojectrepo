# Generated by Django 4.1.2 on 2022-10-09 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllifChartOfAccountsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('statement', models.CharField(blank=True, choices=[('Income Statement', 'Income Statement'), ('Balance Sheet', 'Balance Sheet')], max_length=20, null=True)),
                ('category', models.CharField(blank=True, choices=[('Assets', 'Assets'), ('Liabilities', 'Liabilities'), ('Equity', 'Equity'), ('Revenue', 'Revenue'), ('Expenses', 'Expenses')], max_length=20, null=True)),
                ('nature', models.CharField(blank=True, choices=[('Debit', 'Debit'), ('Credit', 'Credit'), ('Both', 'Both')], max_length=20, null=True)),
                ('type', models.CharField(blank=True, choices=[('Posting', 'Posting'), ('Heading', 'Heading'), ('Total', 'Total'), ('Begin-Total', 'Begin-Total'), ('End-Total', 'End-Total')], max_length=20, null=True)),
                ('balance', models.FloatField(blank=True, default=0, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlwenAssetsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('value', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('lifespan', models.CharField(blank=True, max_length=10, null=True)),
                ('acquired', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlwenDriversModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='logistics/images/vehicles/%Y/')),
                ('driver_license', models.FileField(blank=True, null=True, upload_to='logistics/images/vehicles/%Y/')),
                ('driver_id', models.FileField(blank=True, null=True, upload_to='logistics/images/vehicles/%Y/')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenExpensesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=25, null=True)),
                ('amount', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlwenServiceDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_number', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('odometer', models.IntegerField(blank=True, null=True)),
                ('service_center', models.CharField(blank=True, max_length=30, null=True)),
                ('service_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('receipt', models.FileField(blank=True, null=True, upload_to='myfiles/')),
                ('serviced_by', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlwenVehiclesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_image', models.ImageField(blank=True, null=True, upload_to='logistics/images/vehicles/%Y/')),
                ('vehicle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('vehicle_make', models.CharField(blank=True, max_length=30, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=30, null=True)),
                ('year', models.CharField(blank=True, max_length=30, null=True)),
                ('starting_odometer', models.IntegerField(blank=True, default=0, null=True)),
                ('primary_meter', models.CharField(blank=True, choices=[('Kilometers', 'Kilometers'), ('Miles', 'Miles')], default='Kilometers', max_length=30, null=True)),
                ('vehicle_type', models.CharField(blank=True, choices=[('Truck', 'Truck'), ('Car', 'Car'), ('Pickup', 'Pickup'), ('Bus', 'Bus'), ('Trailer', 'Trailer'), ('Van', 'Van'), ('Tow Truck', 'Tow Truck'), ('Motorcycle', 'Motorcycle')], max_length=30, null=True)),
                ('vehicle_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=30, null=True)),
                ('mydocument', models.FileField(blank=True, null=True, upload_to='myfiles/')),
                ('oil_type', models.CharField(blank=True, choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], max_length=30, null=True)),
                ('oil_capacity', models.CharField(blank=True, max_length=30, null=True)),
                ('fuel_usage', models.IntegerField(blank=True, default=0, null=True)),
                ('comments', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwendriversmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CardsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('number', models.IntegerField(default=0, null=True)),
                ('balance', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.CharField(blank=True, default='No comment', max_length=15, null=True)),
                ('currency', models.CharField(blank=True, choices=[('KES', 'KES'), ('$', 'USD'), ('€', 'EURO')], default=1, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarriersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.CharField(blank=True, choices=[('Truck', 'Truck'), ('Car', 'Car'), ('Pickup', 'Pickup'), ('Aeropplane', 'Aeropplane'), ('Ship', 'Ship'), ('Bus', 'Bus'), ('Trailer', 'Trailer'), ('Van', 'Van'), ('Bajaaj', 'Bajaaj'), ('Bike', 'Bike'), ('Other', 'Other')], max_length=30)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, choices=[('KGs', 'KGs'), ('Ton', 'Ton'), ('Other', 'Other')], max_length=20, null=True)),
                ('owner', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, choices=[('Somalia', 'Somalia'), ('Somaliland', 'Somaliland'), ('Kenya', 'Kenya'), ('UAE', 'UAE'), ('Ethiopia', 'Ethiopia'), ('Other', 'Other')], max_length=30)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('contact', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('expected', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Booked', 'Booked'), ('Loaded', 'Loaded'), ('Dispatched', 'Dispatched'), ('Enroute', 'Enroute'), ('Delivered', 'Delivered'), ('Unknown', 'Unknown'), ('Other', 'Other')], default='Booked', max_length=20, null=True)),
                ('origin', models.CharField(blank=True, max_length=20, null=True)),
                ('destination', models.CharField(blank=True, max_length=20, null=True)),
                ('via', models.CharField(blank=True, choices=[('Road', 'Road'), ('Air', 'Air'), ('Sea', 'Sea')], default='Road', max_length=20, null=True)),
                ('shipment_number', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=30, null=True)),
                ('carrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrier_related', to='logistics.alwenvehiclesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('units', models.CharField(blank=True, choices=[('KGs', 'KGs'), ('Ton', 'Ton')], default='KGs', max_length=20, null=True)),
                ('lenth', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('dimension_units', models.CharField(blank=True, choices=[('m', 'm'), ('cm', 'cm'), ('mm', 'mm')], default='CM', max_length=20, null=True)),
                ('received', models.DateTimeField(blank=True, null=True)),
                ('value', models.CharField(blank=True, max_length=20, null=True)),
                ('rate', models.CharField(blank=True, max_length=20, null=True)),
                ('payment', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('Received', 'Received'), ('Booked', 'Booked'), ('Loaded', 'Loaded'), ('Dispatched', 'Dispatched'), ('Enroute', 'Enroute'), ('Delivered', 'Delivered')], default='Received', max_length=20, null=True)),
                ('destination', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=20, null=True)),
                ('consignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consigneerelated', to='logistics.customersmodel')),
                ('consigner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consignerrelated', to='logistics.customersmodel')),
                ('payer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payerrelated', to='logistics.customersmodel')),
                ('shipment_items_connector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipmentanditemrelatedname', to='logistics.shipmentsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTasksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=20, null=True)),
                ('spares_cost', models.IntegerField(blank=True, default=0, null=True)),
                ('labor_cost', models.IntegerField(blank=True, default=0, null=True)),
                ('task_service_connector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskrelated', to='logistics.alwenservicedetailsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPaymentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('comments', models.CharField(blank=True, default='comment', max_length=15, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custpaymentreltedname', to='logistics.customersmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CardsTopUpsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('comments', models.CharField(blank=True, default='comment', max_length=15, null=True)),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cardreltedname', to='logistics.cardsmodel')),
            ],
        ),
        migrations.AddField(
            model_name='alwenservicedetailsmodel',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwenvehiclesmodel'),
        ),
        migrations.CreateModel(
            name='AlwenJobsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('opened_date', models.DateField(auto_now_add=True, null=True)),
                ('ending_date', models.DateField(blank=True, null=True)),
                ('starting_odometer', models.IntegerField(blank=True, default=0, null=True)),
                ('ending_odometer', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(blank=True, choices=[('open', 'open'), ('completed', 'completed')], default='open', max_length=20, null=True)),
                ('refernce', models.CharField(blank=True, max_length=20, null=True)),
                ('delivery', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=20, null=True)),
                ('uplift', models.FloatField(blank=True, default=1, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobcustrelname', to='logistics.customersmodel')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwendriversmodel')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwenvehiclesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenJobItemsSellingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('unit_cost', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('unit_price', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('jobitselcon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jbitselrenm', to='logistics.alwenjobsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenJobItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('unit_cost', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('unit_price', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('selling_price', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, default='Comments', max_length=20, null=True)),
                ('description', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desrlnm', to='logistics.alwenexpensesmodel')),
                ('jobitemconnector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemjobconrelnme', to='logistics.alwenjobsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenInvoicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(blank=True, max_length=20, null=True)),
                ('invoice_due_Date', models.DateField(blank=True, null=True)),
                ('invoice_terms', models.CharField(choices=[('Cash', 'Cash'), ('Deposit', 'Deposit'), ('15 days', '15 days')], default='Cash', max_length=20)),
                ('invoice_status', models.CharField(choices=[('Paid', 'Paid'), ('Current', 'Current'), ('Overdue', 'Overdue')], default='Current', max_length=20)),
                ('invoice_currency', models.CharField(choices=[('KES', 'KES'), ('$', 'USD'), ('£', 'EURO')], default='$', max_length=20)),
                ('invoice_comments', models.CharField(blank=True, default='invoice', max_length=20, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('invoice_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('posting_inv_status', models.CharField(blank=True, choices=[('waiting', 'waiting'), ('posted', 'posted')], default='waiting', max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alwrelatcustinvoice', to='logistics.customersmodel')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobinvrelnm', to='logistics.alwenjobsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenInvoiceItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('alinvcontr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitemrelated', to='logistics.alweninvoicesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenFillUpsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, null=True)),
                ('odometer', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('oil_type', models.CharField(blank=True, choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], max_length=25, null=True)),
                ('station', models.CharField(blank=True, max_length=25, null=True)),
                ('payment', models.CharField(blank=True, choices=[('KES', 'KES'), ('USD', 'USD'), ('EURO', 'EURO')], max_length=25, null=True)),
                ('receipt', models.FileField(blank=True, null=True, upload_to='myfiles/')),
                ('fuel_brand', models.CharField(blank=True, max_length=25, null=True)),
                ('notes', models.CharField(blank=True, max_length=20, null=True)),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.cardsmodel')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwendriversmodel')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwenvehiclesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenDailyMileageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('starting_odometer', models.IntegerField(blank=True, null=True)),
                ('ending_odometer', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=20, null=True)),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwendriversmodel')),
                ('vehicle', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.alwenvehiclesmodel')),
            ],
        ),
    ]
