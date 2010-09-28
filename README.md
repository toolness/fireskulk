Fireskulk is a simple proof-of-concept that makes it relatively easy to create new browsers on Mac OS X which look suspiciously like Firefox.

## Rationale ##

This experiment is based on the following assumptions:

* People don't use multiple browsers because they like their different strengths and weaknesses, but because their browsing habits are so diverse that they prefer to compartmentalize them within different usage scenarios: they may use Firefox for work, Chrome for personal use, and Safari as an alternative to private browsing mode.

* Firefox [Profiles][], aside from being difficult to configure and use, also lack a variety of affordances that are present in separate browser products. For instance, Firefox and Chrome have different icons and application names, which is of immense aid when navigating between different contexts.

## Use ##

To use Fireskulk:

  1. Create a directory called `.fireskulk` in your home directory.

  2. In this directory, create a subdirectory called whatever you want to name your new browser. If you want to call it `Workfox`, for instance, create a new directory called `~/.fireskulk/Workfox`.

  3. Put an icon file in this directory called `firefox.icns`. This will be used as the new browser's application icon. You can use Icon Composer to do this, which comes with OS X's developer tools.

  4. Run `fireskulk.py`. This will place new browsers in your `/Applications` directory.

## Limitations ##

Fireskulk works by cloning `/Applications/Firefox.app` and invasively modifying its OS X and XULRunner metadata. Software update is almost guaranteed to be broken.

  [Profiles]: http://support.mozilla.com/en-US/kb/managing+profiles
