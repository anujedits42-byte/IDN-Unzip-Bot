# Copyright (c) 2021 Itz-fork
# Edited IDN-C-X

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Help 📜", callback_data="helpcallback"),
                InlineKeyboardButton("About ⁉️", callback_data="aboutcallback")
            ]
        ]
    )
    
    CHOOSE_E_BTN=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("File Extract 📂", callback_data="extract_file|tg_file|no_pass"),
                InlineKeyboardButton("File (Password) Extract 📂", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("🔗 Url Extract 📂", callback_data="extract_file|url|no_pass"),
                InlineKeyboardButton("🔗 (Password) Url Extract 📂", callback_data="extract_file|url|with_pass")
            ],
            [
                InlineKeyboardButton("Cancel ❌", callback_data="cancel_dis")
            ]
        ]
    )

    CLN_BTNS=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Clean My Files 😇", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("TF! Nooo 😳", callback_data="nobully")
            ]
        ]
    )
    
    ME_GOIN_HOME=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back 🏡", callback_data="megoinhome")
            ]
        ]
    )


class Messages:
    START_TEXT = """
Hi **{}**, I'm **Ak Unzipper Bot** 😇!

`I can extract archives like zip, rar, tar etc.`

**Made with ❤️ by @Anujedits76**
    """

    HELP_TXT = """
**How To Extract? 🤔**
`1. Send the file or link that you want to extract.`
`2. Click on extract button (If you sent a link use "Url Extract" button. If it's a file just use "File Extract" button).`
**Note:**
    **1.** `If your archive is password protected select` **(Password) Extract 📂** `mode. Bot isn't a GOD to know your file's password so If this happens just send that password!`
    
    **2.** `Please don't send corrupted files! If you sent a one by a mistake just send` **/clean** `command!`
    
    **3.** `If your archive have 95 or more files in it then bot can't show all of extracted files to select from. So in that case if you can't see your file in the buttons just click on` "Upload All ♻️" `button. It'll send all extracted files to you!`
    """

    ABOUT_TXT = """
**About Ak Unzip Bot,**
✘ **Language:** [Python](https://www.python.org/)
✘ **Framework:** [Pyrogram](https://docs.pyrogram.org/)
✘ **Source Code:** [Anuj](https://t.me/anujedits76)
✘ **Developer:** [Anuj](https://t.me/anujedits76)
**Made with ❤️ by @anujedits76**
    """

    LOG_TXT = """
**Extract Log 📝!**
**User ID:** `{}`
**File Name:** `{}`
**File Size:** `{}`
    """

    AFTER_OK_DL_TXT = """
**Successfully Downloaded**
**Download time:** `{}`
**Status:** `Trying to extract the archive`
    """

    EXT_OK_TXT = """
**Extraction Successfull!**
**Extraction time:** `{}`
**Status:** `Trying to upload`
    """

    EXT_FAILED_TXT = """
**Extraction Failed 😕!**
**What to do?**
 - `Please make sure archive isn't corrupted`
 - `Please make sure that you selected the right mode!`
 - `May be Your archive format isn't supported 😔`
**Please report this at @IDNCoderX if you think this is a serious error**
    """

    ERROR_TXT = """
**Error Happend 😕!**
**ERROR:** {}
**Please report this at @anujedits76 if you think this is a serious error**
    """

    CANCELLED_TXT = """
**{} ✅!**
`Now all of your files have been deleted from my server 😏!`
    """

    CLEAN_TXT = """
**Are sure want to delete your files from my server 🤔?**
**Note:** `This action cannot be undone!`
    """


# List of error messages from p7zip
ERROR_MSGS = [
    "Error",
    "Can't open as archive"
    ]
