import os


def get_encryption_params():
    print ('***[SecurityEncryption] GNS_PROFILE is ', os.environ['GNS_PROFILE'])
    if os.environ['GNS_PROFILE'] == 'LAB':
        return {
            'key': '/etc/httpd/ssl/vmdev-cmt61.socdev.intelsat.com.key',
            'crt': '/etc/httpd/ssl/vmdev-cmt61.socdev.intelsat.com.cer'
        }
    elif os.environ['GNS_PROFILE'] == 'MCC' or os.environ['GNS_PROFILE'] == 'POV':
        return {
            'key': '/etc/httpd/ssl/socit.intelsat.com.key',
            'crt': '/etc/httpd/ssl/socit.intelsat.com.crt'
        }
    elif os.environ['GNS_PROFILE'] == 'ESOC' or os.environ['GNS_PROFILE'] == 'LSOC':
        return {
            'key': '/etc/httpd/ssl/soc.intelsat.com.key',
            'crt': '/etc/httpd/ssl/soc.intelsat.com.crt'
        }

