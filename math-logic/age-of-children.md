# Age of children

*This problem is from the book "In code: a mathematical journey" by Sarah Flannery and David Flannery.*

A (presumed smart) insurance agent knocks on a door and a (presumed smart) woman opens.  He introduces himself and asks if she has any children.

She answers: 3.  When he then asks their ages (which for this problem we abstract to integers), she hesitates.  Then she decides to give him some information about their ages, saying "the product of their ages is 36".  He asks for more information and she gives in, saying "the sum of their ages is equal to our neighbors' house number". The man jumps over the fence, inspects the house number, and the returns. "You need to give me another hint", he begs.  "Alright", she says, "my oldest child plays the piano".  What are the ages of the children?

## Solution

2, 2, 9

There are 8 ways to get 36 as the product of the ages. When doing the sum, two of them get the same result, so the extra fact helps to know that the oldest is just one

    36 = 1*1*36 = 38
    36 = 1*2*18 = 21
    36 = 1*3*12 = 16
    36 = 1*4*9  = 14
    36 = 1*6*6  = 13
    36 = 2*2*9  = 13 <<<
    36 = 2*3*6  = 11
    36 = 3*3*4  = 10