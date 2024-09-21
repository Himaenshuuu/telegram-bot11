import telegram.ext
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import asyncio

# Bot token
Token = "7594042648:AAE-bkTnDCym9hgTVSuqRnqKOpzSdIN8jtQ"


# Define command handlers
async def help_command(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Available Commands:
/start    -> Welcome to the channel
/help     -> How can I assist you?
/content  -> Information about the content provided by us
/contact  -> Contact information
/photos   -> View photos
    """
    )
async def content(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Available Commands:
/start    -> Welcome to the channel
/help     -> How can I assist you?
/content  -> Information about the content provided by us
/contact  -> Contact information
/photos   -> View photos
/mess     -> This is mess menu
    """
    )


async def contact(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are the important contacts.")

async def photos(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are some photos.")

async def start(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to the channel.")

async def mess(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    # Send the document directly from the local file system
    with open("Copy of MENU-SEP.pdf", "rb") as file:
        await update.message.reply_document(document=file, caption="Mess-menu")
    
# Main function to set up and run the bot
async def main():
    # Create the Application and add command handlers
    application = ApplicationBuilder().token(Token).build()

    # Adding handlers for different commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("content", content))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("photos", photos))
    application.add_handler(CommandHandler("mess", mess))

    # Initialize and start the application
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    # Keep running until manually interrupted (Ctrl+C)
    await application.idle()


# Wrapper to handle event loop in Spyder or Jupyter-like environments
def run_bot():
    try:
        # Get the current event loop
        loop = asyncio.get_event_loop()

        # If the loop is already running, create a task for the bot
        if loop.is_running():
            print("Event loop already running. Running the bot as a background task.")
            loop.create_task(main())  # Create a task for the bot's main function
        else:
            # If the loop isn't running, run the bot normally
            loop.run_until_complete(main())

    except RuntimeError as e:
        print(f"Runtime Error: {e}")


# Run the bot
if __name__ == "__main__":
    run_bot()
