from logzero import logger
import redis
import requests

def diff_max_and_min(array):
    """
    Returns integer diff between max and min integer in array.
    If array contains any numerical anagrams, returns None.
    """
    def anagram_for(num):
        return int(as_string(num)[::-1])

    def as_string(num):
        return str(num, 'utf-8') if isinstance(num, bytes) else str(num)

    def as_int(num):
        return int(as_string(num))

    checked = []
    for item in array:
        # logger.debug('item: %s' % (item,))
        if anagram_for(item) in checked:
            return None
        checked.append(as_int(item))

    return max(checked) - min(checked)


def main():
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

        diff = diff_max_and_min(val)
        logger.info('diff: %s' % (diff,))

        if diff:
            checksum += diff

    logger.info('checksum: %s' % checksum)

    url = "http://answer:3000/%s" % checksum
    logger.info('url: %s' % url)

    response = requests.get(url)
    logger.info('response: %s' % response)

    logger.info('done.')


if __name__ == "__main__":
    main()
