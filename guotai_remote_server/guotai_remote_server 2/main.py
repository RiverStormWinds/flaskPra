import datetime
import web

from model import TrainModel
from code import CalModelMerge

urls = (
    '/predict', CalModelMerge,
    '/training', TrainModel
)

if __name__ == "__main__":
    web.config.debug = False
    start_time = datetime.datetime.now()
    app = web.application(urls, globals())
    app.run()
    end_time = datetime.datetime.now()
    run_time = (start_time - end_time).seconds
    print(run_time)
