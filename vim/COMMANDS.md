# vim Commands

`vim` is an interactive Text Editor application that runs in a Terminal Emulator and is keyboard-based, without any mouse interaction.

Editing and managing files in `vim` requires stateful commands and interactions.

There are 5 Modes in `vim`:

1. Normal
2. Command
3. Input
4. Visual
5. Replace

Text can only be entered into the file currently being edited when in **Input** mode.

Since `vim` is keyboard-based, all commands and controls are managed through key combinations and sequences. For readability, all latin characters will be represented in lowercase, and uppercase characters will not be used. When an uppercase character is needed, the key combination `SHIFT+r` will be used instead of `R`.

Technically, `vim` relies on the UTF/ASCII keycodes so `r` and `R` are different keys/characters. This means that if you can press `R` without shift, like by using `CAPSLOCK`, then `vim` will recognize it as `R` and not `r`. So if you have `CAPSLOCK` on and you press `SHIFT+r`, you'd be entering `r`.

Arguably, that's probably why a lot of `vim` documentation uses the uppercase and lowercase characters, for accuracy, but I currently find that potentially misleading or hard to read. So, under the risk of this documentation making no sense if you have `CAPSLOCK` on, I'd rather use `SHIFT+r` instead of `R`.

Probably 'cause I'm not smart and would otherwise confuse myself. So take this as you may.

## Info

Tested with `vim` version: `8.2` (2019-12-12)

Last Updated: 2020-03-15

Documentation is in reference to a US Keyboard standard layout, lowercase (base) characters only. Uppercase (alternate) characters are represented as a key combination of the `SHIFT` key and the lowercase (base) character.

Examples:

- `R` is shown as `SHIFT+r`
- `&` is shown as `SHIFT+7`
- `:` is shown as `SHIFT+;`
- `=` is shown as `=`
- `+` is shown as `SHIFT+=`

## Normal Mode

**Normal** mode is the default state of `vim`. From any other mode, you can return to **Normal** mode by pressing the `ESC` key.

Mode features:

- Text Editing: No
- Navigation with Arrows: yes
- Navigation with Letters: yes
- Selection: No
- Cut: Yes
- Copy: Yes
- Paste: Yes
- Delete: Yes

### Cut, Copy, Paste


#### References

- https://vim.fandom.com/wiki/Copy,_cut_and_paste

## Command Mode

**Command** mode is the internal commandline of `vim` where you can manage and update the application. **Command** mode is indicated by the `:` character, and is entered into from Normal mode by pressing the `;` key.

Mode features:

- Text Editing: No
- Navigation with Arrows: No
- Navigation with Letters: No
- Selection: No
- Cut: No
- Copy: No
- Paste: No
- Delete: No

### Save New File

You can start `vim` without a pre-existing file. In this case, you are in a new file, so to save it, you need to write it out to the filesystem.

Writing-out a new file is essentially a `"Save as..."` operation:

```vim
:w /path/to/new_file.ext
```
or

```vim
:saveas /path/to/new_file.ext
```

When you make any follow-up edits and want to save the current edits to the file:

```vim
:w
```

### Close Current File

Technically, file views in `vim` are known as "Buffers" (for more details, see the #Buffers section).

If you wanted to just close everything and quit `vim` you can use:

```vim
:q
```

However, if you want `vim` to stay open, but you want to close the current Buffer (file) you have a few options.

View all the open/available buffers:

```vim
:bufffers
```

Closing the Buffer without removing it:

```vim
:bd
```


### Open Existing File

## Insert Mode

## Visual Mode

## Replace Mode

**Replace** mode has two forms:

- Single-character replacement mode: `r` from **Normal** Mode
- Extended replacement mode: `SHIFT+r` from **Normal** Mode

Mode features:

- Text Editing: Yes
- Navigation with Arrows: Yes
- Navigation with Letters: No
- Selection: No
- Cut: No
- Copy: No
- Paste: No
- Delete: No

In **Replace** mode, this is similar to some shells or text editors that support the `INSERT` key; text will be overwritten under the cursor.

Technically, **Replace** mode is a special circumstance of **Insert** mode; so if you have the State/Mode shown in `vim` it will show `-- INSERT --` as the mode.


### Single-Character Replacement

From **Normal** mode, you press the `r` key to enter this mode, and then the next character you press will replace the character under/after the cursor.

Single-Character replacement means that you can only press a single character before returning to the previous mode.

When you're in **Visual** mode, if you've visually selected multiple characters and then you press the `r` key to enter into **Replace** mode, the next key will replace the first character, or the first character per line, within the selection.


### Extended Replacement


## Buffers


### Name an Unnamed Buffer

If you are in a current buffer, you can name it `new_name` with:

```vim
:e new_name
```

You can then verify the buffer names with:

```vim
:buffers
```

## Windows


## Undo Branches


### References

- https://vim.fandom.com/wiki/Using_undo_branches

# References

- https://vimhelp.org/
- https://vimhelp.org/vim_faq.txt.html
- https://guide.freecodecamp.org/vim
