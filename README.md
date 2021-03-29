# app_test

日志:

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("invoke " + func.__name__ + "\n args \n" + repr(args[1:]) + repr(kwargs))
```
