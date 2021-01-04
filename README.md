# Google Sheets FMC Solution Checker
A Google Sheets document that can verify FMC solutions using an external REST API.

Some usages:

<img src="solution-checker.gif">

<img src="solution-checker-2.gif">

---

# But... how??

Did you know Google Sheets has *so* much more than you thought?  
As in: you can actually write your own functions and use them on the sheet. Like, really anything you want.

Check out this feature on the `Tools > Script Editor` menu.

In this case, I wrote the thing on the `solution-checker.gs` file, which is just a single function called `checkSolutions`... and does just that.  
For each row, it sends a GET request to my REST API using the values on the column `A`, which are the solutions some people could have submitted using a form or something, and a fixed scramble.

> *Note: the API only supports notation that is valid for the WCA FMC event, except the useless "2Fw" type of moves which should be removed from the regulations as soon as possible. You can learn more about it [here](https://www.worldcubeassociation.org/regulations/#12a).*

The API then returns an integer which will be the length of the solution in case it was correct, or `-1` otherwise.  
These values are afterwards written down on the sheet on the column `B` labelled as "Results".

As it is now, the function is triggered every time the form associated to the Sheet is sent, but you can set other triggers such as: on Sheet reload, on X amount of time, etc., by going to the Script Trigger tab on the Edit menu within the Script Editor.

# Can I use this?

Sure, I don't mind at all. I did this for Marlon de V. Marques on a lazy Sunday.  
If you want to recreate this, you just have to create a `.gs` file on your Google Sheet, set it up like mine, and just paste my code.  
Or you could change the queries within the Sheet, because mine are a bit clumsy (I didn't bother too much with that because the format will quite likely change).

Otherwise, if you just want the API, consume it like this:

```
https://solution-checker.guidodipietro.repl.co/<scramble>/<solution>
```

or check the live REPL.IT [here](https://repl.it/@GuidoDipietro/solution-checker).

# Thanks

No poblers
