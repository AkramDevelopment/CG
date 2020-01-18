import logging
import datetime





def log_unban(unbanned_by,unbanned_email):
    unban_logger = logging.getLogger(__name__)
    unban_logs = logging.FileHandler('logs/unbans.log')
    unban_logger.addHandler(unban_logs)
    unban_logger.setLevel(logging.CRITICAL)
    unban_logger.critical(f'{unbanned_email} was unbanned by {unbanned_by} on {datetime.datetime.now()}')
    
    


def post_removed(removed_by,post_id):
    post_logger = logging.getLogger(__name__)
    post_logs = logging.FileHandler('backend/logging/logs/post_removed.log')
    post_logger.addHandler(post_logs)
    post_logger.setLevel(logging.CRITICAL)
    post_logger.critical(f'post deleted by (id = {post_id}) by {removed_by} on {datetime.datetime.now()}')




def announcement_removed(removed_by,announcement_id):
    announcement_logger = logging.getLogger(__name__)
    announcement_logs = logging.FileHandler('/backend/logging/logs/announcement_removed.log')
    announcement_logger.addHandler(announcement_logs)
    announcement_logger.setLevel(logging.CRITICAL)
    announcement_logger.critical(f'Announcement removed (id={announcement_id}) by {removed_by} on {datetime.datetime.now()}')



