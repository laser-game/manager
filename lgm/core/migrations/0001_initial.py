# Generated by Django 2.0.6 on 2018-06-24 22:40

import core.utils.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


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
                ('identifier', models.CharField(choices=[('K', 'player kill player'), ('F', 'friendly fire'), ('T', 'trap'), ('B', 'bonus')], max_length=1, verbose_name='Identifier')),
                ('time', models.DurationField(verbose_name='Time elapsed from start of game')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('game_mode', models.CharField(choices=[('S', 'solo'), ('T', 'team')], max_length=1, verbose_name='Game mode')),
                ('button_action_mode', models.CharField(choices=[('D', 'disable'), ('F', 'fuse'), ('W', 'white flashlight'), ('U', 'ultra violet flashlight')], max_length=1, verbose_name='Mode of button action')),
                ('sound_set_type', models.CharField(choices=[('CZ', 'czech'), ('EN', 'english')], max_length=2, verbose_name='Set of sounds')),
                ('game_duration', models.DurationField(validators=[core.utils.validators.MinDurationValidator(60), core.utils.validators.MaxDurationValidator(1800)], verbose_name='Time duration of game')),
                ('death_duration', models.DurationField(validators=[core.utils.validators.MinDurationValidator(1), core.utils.validators.MaxDurationValidator(30)], verbose_name='Time duration of death state')),
                ('batch_shots_count', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Count of shots in batch')),
                ('enable_sound', models.BooleanField(verbose_name='Enable sound')),
                ('enable_vest_light', models.BooleanField(verbose_name='Enable vest light')),
                ('enable_immorality', models.BooleanField(verbose_name='Enable immorality')),
                ('state', models.CharField(choices=[('S', 'set'), ('P', 'play'), ('B', 'break'), ('D', 'done')], max_length=1, verbose_name='State of game')),
                ('created_time', models.DateTimeField(verbose_name='Created time')),
                ('started_time', models.DateTimeField(blank=True, null=True, verbose_name='Started time')),
                ('elapsed_time', models.DurationField(blank=True, null=True, verbose_name='Elapsed time')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('position', models.PositiveSmallIntegerField(verbose_name='Player position')),
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
            name='GameTeam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('position', models.PositiveSmallIntegerField(verbose_name='Player position')),
                ('points', models.IntegerField(verbose_name='Total points')),
                ('shots_count', models.PositiveSmallIntegerField(verbose_name='Count of shots')),
                ('kills_count', models.PositiveSmallIntegerField(verbose_name='Count of kills')),
                ('deaths_count', models.PositiveSmallIntegerField(verbose_name='Count of deaths')),
                ('friendly_kills_count', models.PositiveSmallIntegerField(verbose_name='Count of friendly kills')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_team_game', to='core.Game')),
            ],
            options={
                'verbose_name': 'Game team',
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
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('time_on', models.DurationField(verbose_name='Time of switch')),
                ('event', models.CharField(choices=[('D', 'disable'), ('C', 'after configuration'), ('S', 'after start'), ('E', 'after end')], max_length=1, verbose_name='Switch event')),
            ],
            options={
                'verbose_name': 'Switch',
                'verbose_name_plural': 'switches',
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
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
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
                'verbose_name': 'Type color',
                'verbose_name_plural': 'Types colors',
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
                ('sound_set_type', models.CharField(choices=[('CZ', 'czech'), ('EN', 'english')], max_length=2, verbose_name='Set of sounds')),
                ('game_duration', models.DurationField(validators=[core.utils.validators.MinDurationValidator(60), core.utils.validators.MaxDurationValidator(1800)], verbose_name='Time duration of game')),
                ('death_duration', models.DurationField(validators=[core.utils.validators.MinDurationValidator(1), core.utils.validators.MaxDurationValidator(30)], verbose_name='Time duration of death state')),
                ('batch_shots_count', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Count of shots in batch')),
                ('enable_sound', models.BooleanField(verbose_name='Enable sound')),
                ('enable_vest_light', models.BooleanField(verbose_name='Enable vest light')),
                ('enable_immorality', models.BooleanField(verbose_name='Enable immorality')),
            ],
            options={
                'verbose_name': 'Type game',
                'verbose_name_plural': 'Types games',
            },
        ),
        migrations.CreateModel(
            name='TypeGameSwitch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('switch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_game_switch_switch', to='core.Switch')),
                ('type_game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_game_switch_type_game', to='core.TypeGame')),
            ],
            options={
                'verbose_name': 'Type Game Switch',
                'verbose_name_plural': 'Type Game Switches',
            },
        ),
        migrations.CreateModel(
            name='TypeSwitch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('index', models.PositiveSmallIntegerField(verbose_name='Index of switch')),
                ('enable', models.BooleanField(verbose_name='Enable switch')),
            ],
            options={
                'verbose_name': 'Type switch',
                'verbose_name_plural': 'Type switches',
            },
        ),
        migrations.CreateModel(
            name='Vest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('address', models.PositiveSmallIntegerField(verbose_name='Address of vest')),
                ('battery', models.PositiveSmallIntegerField(verbose_name='Battery')),
                ('enable', models.BooleanField(verbose_name='Enable vest')),
                ('online', models.BooleanField(verbose_name='Online vest')),
                ('has_failure', models.BooleanField(verbose_name='Has failure')),
            ],
            options={
                'verbose_name': 'Vest',
                'verbose_name_plural': 'Vests',
            },
        ),
        migrations.AddField(
            model_name='switch',
            name='type_switch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='switch_type_switch', to='core.TypeSwitch'),
        ),
        migrations.AddField(
            model_name='gameteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_team_team', to='core.Team'),
        ),
        migrations.AddField(
            model_name='gameteam',
            name='type_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_team_type_color', to='core.TypeColor'),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='game_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_player_game_team', to='core.GameTeam'),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_player_player', to='core.Player'),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='type_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_player_type_color', to='core.TypeColor'),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='vest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_player_vest', to='core.Vest'),
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_game', to='core.Game'),
        ),
        migrations.AddField(
            model_name='event',
            name='game_player1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='event_game_player1', to='core.GamePlayer'),
        ),
        migrations.AddField(
            model_name='event',
            name='game_player2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='event_game_player2', to='core.GamePlayer'),
        ),
    ]
