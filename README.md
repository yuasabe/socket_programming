## Socket Programming Chat App with Python

Basic chat app made with Python using sockets. All messages are sent with UDP packets, design as below.

## Usage

### To launch sender

```
$ python3 sender.py
```

### To launch receiver

```
$ python3 receiver.py
```

## Packet Format

Messages are sent using UDP with data in the following format:

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|      LEN      |                      DATA                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Note that LEN describes the length of the message DATA, with a max value of 255 (being 8 bits). Therefore, the message DATA can only be 255 bytes in length.