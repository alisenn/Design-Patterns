# STRATEGY

Define a family of algorithms, encapsulate each one, and make them interchangeable.

## When to use
When you want to define a class that will have one behaviour that is similar to others. For example, fly , not fly, fly with wings etc.
### Pros
    - Replace inheritance with compositon
    - Open/Closed princible is satisfied.
    - Hide the complication of implementation from client.
### Cons
    - Lots of classes