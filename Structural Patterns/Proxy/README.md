# Proxy

## Problem
There is an instance of a class and you need to control the acces of the other objects to that one class, because of security reasons, 
and to control the number of instances that reaches the object.

## Solution
Implement an interface that have exactly the same methods with the real object that you want to control the access.
Implement another class that extends this interface, so this class can filter the client and control the access of the real object.
Client won't know if it is the real object or the proxy because both are implementing the same interface

### Command For Running the Code
```
mvn clean && mvn install -DskipDeploy=false -DimageVersion=v3.2-production -Denvironment=Production -DawsRegion=us-east-1
```

## Real World Analogy
A credit card is a proxy for a bank account, which is a proxy for a bundle of cash. Cash and Credit card can be used for payment, both
implements the same interface.