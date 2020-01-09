import logging
import datetime

def account_created(email):
    account_logger = logging.getLogger(__name__)
    account_logs = logging.FileHandler('logs/account_logs.log')
    account_logger.addHandler(account_logs)
    account_logger.setLevel(logging.CRITICAL)
    account_logger.critical(f'{email} was created on {datetime.datetime.now()}')
    

def log_ban(banned_by,banned_email):
    ban_logger = logging.getLogger(__name__)
    ban_logs = logging.FileHandler('logs/bans.log')
    ban_logger.addHandler(ban_logs)
    ban_logger.setLevel(logging.CRITICAL)
    ban_logger.critical(f'{banned_email} was banned by {banned_by} on {datetime.datetime.now()}')
    


def log_unban(unbanned_by,unbanned_email):
    unban_logger = logging.getLogger(__name__)
    unban_logs = logging.FileHandler('logs/unbans.log')
    unban_logger.addHandler(unban_logs)
    unban_logger.setLevel(logging.CRITICAL)
    unban_logger.critical(f'{unbanned_email} was unbanned by {unbanned_by} on {datetime.datetime.now()}')
    


def post_created(created_by,post_id):
    post_logger = logging.getLogger(__name__)
    post_logs = logging.FileHandler('logs/post_created.log')
    post_logger.addHandler(post_logs)
    post_logger.setLevel(logging.CRITICAL)
    post_logger.critical(f'post created (id = {post_id}) by {created_by} on {datetime.datetime.now()}')
    


def post_removed(removed_by,post_id):
    post_logger = logging.getLogger(__name__)
    post_logs = logging.FileHandler('logs/post_removed.log')
    post_logger.addHandler(post_logs)
    post_logger.setLevel(logging.CRITICAL)
    post_logger.critical(f'post deleted by (id = {post_id}) by {removed_by} on {datetime.datetime.now()}')


def announcement_created(created_by,announcement_id):
    announcement_logger = logging.getLogger(__name__)
    announcement_logs = logging.FileHandler('logs/announcement_created.log')
    announcement_logger.addHandler(announcement_logs)
    announcement_logger.setLevel(logging.CRITICAL)
    announcement_logger.critical(f'Announcement created (id={announcement_id}) by {created_by} on {datetime.datetime.now()}')


def announcement_removed(removed_by,announcement_id):
    announcement_logger = logging.getLogger(__name__)
    announcement_logs = logging.FileHandler('logs/announcement_removed.log')
    announcement_logger.addHandler(announcement_logs)
    announcement_logger.setLevel(logging.CRITICAL)
    announcement_logger.critical(f'Announcement removed (id={announcement_id}) by {removed_by} on {datetime.datetime.now()}')





