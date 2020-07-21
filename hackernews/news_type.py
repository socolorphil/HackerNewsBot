import aiohttp

# Returns the top 100 IDs for the following types:
# [Jobs, Stories (New, Top, Best)]

class getType:

  # Utilizes the aiohttp library to access the type of stories the user requests,
  # and turns it into a JSON. Then, it stores the first 100 IDs into a list, which
  # will be returned and then used to display the news.

  # TO DO: Take into account the user's preference
  # (Maybe use a thesaurus library or include our own for some topics)
  # i.e cloud = google drive, onedrive, etc.
  # i.e database = mongodb, mysql, postgresql

  async def get_stories(self, type, BASE_URL):
    async with aiohttp.ClientSession() as session:
      async with session.get(
        BASE_URL + type + '.json?print=pretty') as top_ids:
        data = await top_ids.json()
        count = 0
        ITEM_ID = []
        while count < 100 and len(data) > count:
          ITEM_ID.append(data[count])
          count += 1
        return ITEM_ID