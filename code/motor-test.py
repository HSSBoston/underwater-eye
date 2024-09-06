import explorerhat, time

explorerhat.motor.one.forwards(75)
time.sleep(5)
explorerhat.motor.one.stop()

time.sleep(3)

explorerhat.motor.one.backwards(75)
time.sleep(5)
explorerhat.motor.one.stop()



