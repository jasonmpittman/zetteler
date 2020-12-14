# Zetteler

## Technologies
1. Python 3
2. Markdown

## Basic Overview
Zetteler automates the creation of zettels based on your defined types. 

I created zetteler out of a need for a low friction zettel creation tool. The normal work pattern ([example](https://zettelkasten.de/posts/dan-sheffler-workflow/)) takes you out of a research flow just to create a new zettel. Personally, I found this too jarring. Further, I found most of us repeatedly create identical or at least similar zettels in terms of structure. Thus, typing and retyping the same zettel content is laborious, wasteful, and inefficient. 

Thus, as a tool, zetteler is designed to be unobtrusive and minimally invasive. You define your zettel types in a plaintext `ini` configuration file and use a simple shell command to create new zettels. This works especially well for standardized zettel structures such as academic literature reviews.

## Implementation Instructions
1. Clone this repo:  
    `git clone https://github.com/jasonmpittman/zetteler.git`  

2. Add a symlink into your PATH:  
    `sudo ln -s /path/to/zetteler/new_zettel.py /usr/local/bin/zetteler`  

    If you're on Windows, the above will work in WSL. If you don't use WSL, you're on your own, pal.

3. Define your types in the `types.ini` configuration file. The expected configuration includes a `[type]` followed by the default `tags` and `fields`. Tags are self explanatory. Fields are equivalent to sections and provide a way to segment a zettel.

## Basic Usage
From your shell, run `zetteler [type]` for a quick start. The `Title` will not be completed but the field is present.  

You can also run `zetteler [type] [title]` if you want to include a zettel title from creation.  

A new zettel will be created in **Markdown** with a **YAML** header. The file name is a date and time based `id` such as `202008121531.md`
