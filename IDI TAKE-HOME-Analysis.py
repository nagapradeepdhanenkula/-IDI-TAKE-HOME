{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "390c47a9-c71f-4e57-bee7-64338b3356c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\nagap\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\nagap\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas) (2.0.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\nagap\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\nagap\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\nagap\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\nagap\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8c735676-8c15-4e52-a9b0-368c2655eb24",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "path = \"Copy of correct_twitter_201904.tsv\"\n",
    "df = pd.read_csv(path, sep='\\t', parse_dates=['created_at'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "274ffaab-9acb-4cd5-a64e-af6134beac7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Part2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3e04a94a-417e-4117-b985-0a74769f2c9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def query_data(df, search_term):\n",
    "    # Filter tweets containing the term\n",
    "    mask = df['text'].str.contains(search_term, case=False, na=False)\n",
    "    filtered_df = df[mask]\n",
    "    return filtered_df\n",
    "\t\n",
    "\t# 1. Count tweets per day\n",
    "    daily_counts = filtered_df.groupby(filtered_df['created_at'].dt.date).size()\n",
    " \n",
    "\t# 2. Unique users\n",
    "    unique_users = filtered_df['author_id'].nunique()\n",
    " \n",
    "\t# 3. Average likes\n",
    "    average_likes = filtered_df['like_count'].mean()\n",
    " \n",
    "\t# 4. Origin places\n",
    "    places = filtered_df['place_id'].dropna().unique()\n",
    " \n",
    "\t# 5. Times of day\n",
    "    times_of_day = filtered_df['created_at'].dt.hour.value_counts().sort_index()\n",
    " \n",
    "\t# 6. User with most posts\n",
    "    top_user = filtered_df['author_id'].mode()[0]\n",
    " \n",
    "    return {\n",
    "        \"Daily Counts\": daily_counts,\n",
    "        \"Unique Users\": unique_users,\n",
    "        \"Average Likes\": average_likes,\n",
    "        \"Places\": places,\n",
    "        \"Times of Day\": times_of_day,\n",
    "        \"Top User\": top_user\n",
    "\t}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7c5117f7-6339-4e33-bd30-101f97feda06",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Part3\n",
    "\n",
    "#Setup: Install Python and Pandas (pip install pandas).\n",
    "#Running the Code: Use the function query_data(df, 'places') to get the desired outputs after loading the data as shown.\n",
    "#Pandas is chosen for its ease of use and performance with tabular data, and the system is designed to be run in any Python environment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a3760df-e5fb-4d35-89d8-00c34d7c457b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
