# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
"""
Celery waiter.

Takes orders for files generated by async Celery tasks.
Serves the file when ready. Kindly asks the user to wait if not.

Author: Radek Czajka <radoslaw.czajka@nowoczesnapolska.org.pl>
"""
