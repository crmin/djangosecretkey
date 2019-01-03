import os
from struct import unpack


def generate(length=50):
    sample = '1234567890-=!@#$%^&*()_+qwertyuiopasdfghjklzxcvbnm'
    return ''.join([sample[unpack('>I', os.urandom(4))[0] % len(sample)] for i in range(length)])


def from_file(path):
    """ Load secret key value from file
    If file does not exist, make and generate new secret key value
    :param path: Secret key path
    """
    base_dir = os.path.dirname(path)
    if base_dir:  # if secret key store current dir, base_dir == ''
        try:
            os.makedirs(base_dir, exist_ok=True)  # if path not exist, make it
        except FileExistsError:  # Already exist file (not directory)
            raise NotADirectoryError('{} have to be directory, not file'.format(base_dir))
    secret_key = ''
    if os.path.exists(path):
        if os.path.isfile(path):  # Path exists and it is file
            with open(path, 'r') as f:
                secret_key = f.read().strip()
        else:  # Path exists but, it is not file  --> Error
            raise IsADirectoryError('{} have to be file, not directory'.format(path))
    else:  # Path does not exist --> make and generate secret key
        secret_key = generate()
        with open(path, 'w') as f:
            f.write(secret_key)
    return secret_key


def from_env(env_name='DJANGO_SECRET_KEY'):
    if env_name not in os.environ:  # secret key value does not exists in env
        secret_key = generate()
        os.environ[env_name] = secret_key
        print('** Env variable({}) have to set before run code. **'.format(env_name))
        print('Now, env var {} temporary set to "{}".'.format(env_name, secret_key))
        print('This value preserves when this program is running. '
            'If you guarantee secret key has always same value, '
            'even if restart this program, follow next steps')
        print('1. Open ~/.bashrc (or *rc file) and copy and paste it to bottom of file')
        print('----------------------------------------------------------------')
        print('export {}="{}"'.format(env_name, secret_key))
        print('----------------------------------------------------------------')
        print('2. Save and exit to shell')
        print('3. Run Command:')
        print('-----------------')
        print('source ~/.bashrc')
        print('-----------------')
    return os.environ[env_name]