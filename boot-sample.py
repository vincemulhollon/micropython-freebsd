# This file is executed on every boot (including wake-boot from deepsleep)
# Written by Vince Mulhollon for the micropython-freebsd github project

import esp
esp.osdebug(None)
import gc
gc.collect()

