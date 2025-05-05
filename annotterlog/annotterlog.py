import os
from annotated_logger import AnnotatedLogger
al = AnnotatedLogger(
    name="annotated_logger.example",
    annotations={"branch": os.environ.get("BRANCH", "unknown-branch")}
)
annotate_logs = al.annotate_logs

@annotate_logs()
def split_username(annotated_logger, username):
    annotated_logger.annotate(username=username)
    annotated_logger.info("This is a very important message!", extra={"important": True})
    return list(username)

if __name__=="__main__":
    teste = split_username("nilton.canto")