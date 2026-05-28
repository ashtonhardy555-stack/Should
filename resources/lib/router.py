import sys
import xbmcgui
import xbmcplugin

def route(plugin_url, handle, params):
    """
    Route handler for the RedBox Selector addon
    """
    try:
        # Display a simple menu
        list_item = xbmcgui.ListItem("RedBox Selector")
        xbmcplugin.addDirectoryItem(
            handle,
            url="",
            listitem=list_item,
            isFolder=False
        )
        xbmcplugin.endOfDirectory(handle)
    except Exception as e:
        xbmcgui.Dialog().notification(
            "RedBox Selector",
            f"Error: {str(e)}",
            xbmcgui.NOTIFICATION_ERROR
        )
