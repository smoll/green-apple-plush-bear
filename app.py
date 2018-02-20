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

    def decoded(num):
        return int(str(num, 'utf-8'))

    checked = []
    for item in array:
        # logger.debug('item: %s' % (item,))
        if anagram_for(item) in checked:
            return None
        checked.append(decoded(item))

    return max(checked) - min(checked)

logger.info('starting...')

r = redis.StrictRedis(host='redis', port=6379)
keys = r.keys('*')

checksum = 0
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
        checksum += diff

logger.info('checksum: %s' % checksum)

url = "http://answer:3000/%s" % checksum
logger.info('url: %s' % url)

response = requests.get(url)
logger.info('response: %s' % response)

logger.info('done.')
