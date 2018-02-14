# Generated by Django 2.0.2 on 2018-02-13 01:21

import uuid

import django.core.validators
import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models

import core.utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('time', models.DurationField(verbose_name='Time elapsed from start of game')),
            ],
            options={
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('state', models.CharField(choices=[('S', 'set'), ('P', 'play'), ('B', 'break'), ('D', 'done')], max_length=1, verbose_name='State of game')),
                ('start', models.DateTimeField(verbose_name='Start of game')),
            ],
            options={
                'verbose_name_plural': 'Games',
                'verbose_name': 'Game',
            },
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('vest_index', models.PositiveSmallIntegerField(verbose_name='Index of vest')),
                ('points', models.IntegerField(verbose_name='Total points')),
                ('shots_count', models.PositiveSmallIntegerField(verbose_name='Count of shots')),
                ('kills_count', models.PositiveSmallIntegerField(verbose_name='Count of kills')),
                ('deaths_count', models.PositiveSmallIntegerField(verbose_name='Count of deaths')),
                ('friendly_kills_count', models.PositiveSmallIntegerField(verbose_name='Count of friendly kills')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_player_game', to='core.Game')),
            ],
            options={
                'verbose_name': 'Game player',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email for registered players')),
            ],
            options={
                'verbose_name_plural': 'Players',
                'verbose_name': 'Player',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'verbose_name': 'Team',
            },
        ),
        migrations.CreateModel(
            name='TypeColor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('hw', models.CharField(max_length=7, verbose_name='RGB code for HW')),
                ('css', models.CharField(max_length=7, verbose_name='RGB code for CSS')),
                ('index', models.PositiveSmallIntegerField(verbose_name='Index of color')),
            ],
            options={
                'verbose_name_plural': 'Types colors',
                'verbose_name': 'Type color',
            },
        ),
        migrations.CreateModel(
            name='TypeEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('identifier', models.CharField(choices=[('K', 'player kill player'), ('F', 'friendly fire'), ('T', 'trap'), ('B', 'bonus')], max_length=1, verbose_name='Identifier')),
            ],
            options={
                'verbose_name_plural': 'Types events',
                'verbose_name': 'Type event',
            },
        ),
        migrations.CreateModel(
            name='TypeGame',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('game_mode', models.CharField(choices=[('S', 'solo'), ('T', 'team')], max_length=1, verbose_name='Game mode')),
                ('button_action_mode', models.CharField(choices=[('D', 'disable'), ('F', 'fuse'), ('W', 'white flashlight'), ('U', 'ultra violet flashlight')], max_length=1, verbose_name='Mode of button action')),
                ('sound_set_type', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('E', 'english')], max_length=1, verbose_name='Set of sounds')),
                ('game_duration', models.DurationField(validators=[core.utils.validators.MinDurationValidator(60), core.utils.validators.MaxDurationValidator(1800)], verbose_name='Time duration of game')),
                ('death_duration', models.DurationField(validators=[core.utils.validators.MinDurationValidator(1), core.utils.validators.MaxDurationValidator(30)], verbose_name='Time duration of death state')),
                ('batch_shots_count', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Count of shots in batch')),
                ('enable_sound', models.BooleanField(verbose_name='Enable sound')),
                ('enable_vest_light', models.BooleanField(verbose_name='Enable vest light')),
                ('enable_immorality', models.BooleanField(verbose_name='Enable immorality')),
            ],
            options={
                'verbose_name_plural': 'Types games',
                'verbose_name': 'Type game',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='type_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_type_color', to='core.TypeColor'),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_player_player', to='core.Player'),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_player_team', to='core.Team'),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='type_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_player_type_color', to='core.TypeColor'),
        ),
        migrations.AddField(
            model_name='game',
            name='type_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_type_game', to='core.TypeGame'),
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_game', to='core.Game'),
        ),
        migrations.AddField(
            model_name='event',
            name='type_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_type_event', to='core.TypeEvent'),
        ),
    ]
