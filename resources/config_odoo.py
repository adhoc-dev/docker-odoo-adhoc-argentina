import argparse
import sys
import os
import logging

_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description='Clone repositories and add them to addons_path.')

parser.add_argument(
    'addons_path', metavar='--addons_path', type=str, help='Addons Path')
parser.add_argument(
    'data_dir', metavar='--data_dir', type=str, help='Data Dir')

args = parser.parse_args()

# check addons path exist
data_dir = args.data_dir
addons_path = args.addons_path
modules_to_install = ''

if not os.path.isdir(addons_path):
    _logger.error('Can not locate addons_path %s' % addons_path)
    sys.exit()

# TODO improove and use fabric required
#_logger.info('Starting Postgres')
#os.system("service postgresql start")

odoo_command = (
    "runuser -u odoo odoo.py -- -c /etc/odoo/openerp-server.conf "
    "--stop-after-init -s --unaccent -d odoo --load-language=es_AR "
    "--data-dir=%s --addons-path=%s" % (
        data_dir,
        addons_path,
    ))

_logger.info(
    "Configuring odoo with odoo command:\n%s" % (odoo_command))
os.system(odoo_command)

#_logger.info('Stoping Postgres')
#os.system("service postgresql stop")
