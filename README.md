## crispy [![Test crispy](https://github.com/fybx/crispy/actions/workflows/flow-test_crispy.yml/badge.svg?branch=main)](https://github.com/fybx/crispy/actions/workflows/flow-test_crispy.yml) [![Upload Python Package](https://github.com/fybx/crispy/actions/workflows/flow-publish_package.yml/badge.svg?branch=main)](https://github.com/fybx/crispy/actions/workflows/flow-publish_package.yml)

`crispy` is my take on parsing command-line arguments. It is a dead simple tool that allows you to define your own keys for systematically gathering variables.

In just 5 simple steps, you can start parsing any complicated user input into a dictionary—simple and predictable. It can't get more versatile than that, can it?

### Capabilities

| Feature                                                     | Support | Version     |
|-------------------------------------------------------------|---------|-------------|
| String, integer, float, and boolean type arguments          | ✅      | [v1.0.0][1] |
| Custom exceptions for tracking user errors in input         | ✅      | [v1.0.0][1] |
| Custom subcommands                                          | ✅      | [v2.0.0][2] |
| Positional arguments                                        | ✅      | [v2.1.0][3] |
| Treating quoted strings as single input in `parse_string()` | TO DO   | ...         |

### Usage

1. To start using `crispy-parser` in your projects, install it from [PyPI][0]:

```shell
$ pip install crispy-parser
```

2. Import the parser into your source code:

```python
from crispy.crispy import Crispy
```

3. Add your arguments:

```python
c = Crispy()
c.add_variable("name", str)
c.add_variable("age", int)
c.add_variable("salary", float)
```

4. Throw any user-inputted string or argument list at it!

```python
result = c.parse_string("--name John -a=21 --salary=30000.45")
print(result)
```

> {'name': 'John', 'age': 21, 'salary': 30000.45}

Or parse `sys.argv`:

```python
arguments = c.parse_arguments(sys.argv[1:])
print(arguments)
```

> {'message': 'message.txt', 'targets': 'targets.txt', 'url_format': 'api.txt'}

### Contributing

I welcome contributions to enhance and improve this library! Whether you want to fix a bug, add a new feature, or suggest an improvement, your contributions are highly appreciated.

Just so you know, by contributing to this project, you agree to license your contributions under the same license governing this library. If you're unsure or have questions about the contribution process, please get in touch with me by opening an issue.

## Credits

Feel free to contact me for collaboration on anything!

Ferit Yiğit BALABAN, <[fyb@fybx.dev][llmail]>

[My Website][llwebsite] • [My Bento][llbento] • [X][llx] • [LinkedIn][lllinkedin]

2023

[0]: https://pypi.org/project/crispy-parser/
[1]: https://github.com/fybx/crispy/releases/tag/v1.0.0
[2]: https://github.com/fybx/crispy/releases/tag/v2.0.0
[3]: https://github.com/fybx/crispy/releases/tag/v2.1.0
[llmail]: mailto:fyb@fybx.dev
[llwebsite]: https://fybx.dev
[llbento]: https://bento.me/balaban
[llx]: https://x.com/fybalaban
[lllinkedin]: https://linkedin.com/in/fybx
