from logzero import logger
import redis
import requests

def _diff(array):
    """
    Returns integer diff between max and min integer in array.
    If array contains any numerical anagrams, returns None.
    """
    def anagram_for(num):
        return int(str(num, 'utf-8')[::-1])

    checked = []
    for item in array:
        # logger.debug('item: %s' % (item,))
        if anagram_for(item) in checked:
            return None
        checked.append(int(item))

    return max(checked) - min(checked)

logger.info('starting...')

r = redis.StrictRedis(host='redis', port=6379)
keys = r.keys('*')

total = 0
for key in keys:
    type = r.type(key)
    logger.info('type: %s' % type)

    if type == b'list':
        val = r.lrange(key, 0, -1)
    elif type == b'set':
        val = r.smembers(key)
    else:
        raise BaseException('FIXME: unhandled redis type!')
    logger.info('val: %s' % (val,))

    diff = _diff(val)
    logger.info('diff: %s' % (diff,))

    if diff:
        total += diff

logger.info('total: %s' % total)
logger.info('done.')
