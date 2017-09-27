import yaml


class RequesterConfigLoader:

    def __init__(self, config_path='config.yml'):
        self.config_path = config_path
        self._load()

    def _load(self):
        with open(self.config_path, 'r') as file:
            self._data = yaml.load(file.read())

    def to_celery_beat_schedule(self, schedule_name, task_name):
        celery_beat_schedule = {}
        for index, site in enumerate(self._data['sites']):
            url = site['url']
            delay_in_s = float(site['delay'])/1000
            celery_periodic_task = self._to_celery_periodic_task(
                task_name, delay_in_s, url
            )
            # it's needed to avoid overwriting existing tasks
            schedule_name = "{}_{}".format(schedule_name, index)

            celery_beat_schedule[schedule_name] = celery_periodic_task

        return celery_beat_schedule

    def _to_celery_periodic_task(self, task, delay, *args):
        return {
            'task': task,
            'schedule': delay,
            'args': args
        }