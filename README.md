# beginner-project-solutions
My solutions to the [beginner projects](https://github.com/jorgegonzalez/beginner-projects)

First solution to the problem of 99 bottles of beer
was inspired by a search i made to learn how to inverse
the order of a range.

I discovered that i could just write :

```python
for i in range(99, 0, -1):
    print("something")
```

which simply says to start `i` at `99` and go
down to `0` by decrementing 1 at a time.
