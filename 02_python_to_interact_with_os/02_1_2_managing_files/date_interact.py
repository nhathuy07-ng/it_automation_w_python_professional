#!/usr/bin/env python3

import arrow 

date = arrow.get('23:36 11/08/2026', 'hh:mm DD/MM/YYYY')
print(date.format('dddd, DD MMMM', locale='vi'))
