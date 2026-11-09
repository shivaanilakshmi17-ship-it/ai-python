{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN9rCpzlSRBECRv9OEv3Wt+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shivaanilakshmi17-ship-it/ai-python/blob/main/solution5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xtfJgnqo3Cg3",
        "outputId": "993c594d-2511-4cc8-e34e-2a72bf65c5cc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- Pandas Series ---\n",
            "A    85\n",
            "B    91\n",
            "C    78\n",
            "D    88\n",
            "E    95\n",
            "dtype: int64\n",
            "\n",
            "--- DataFrame ---\n",
            "   RollNo    Name Department  Mark\n",
            "0     101  Anitha        CSE    85\n",
            "1     102    Bala        CSE    91\n",
            "2     103  Chitra        ECE    78\n",
            "3     104  Dinesh        CSE    88\n",
            "4     105   Ezhil        ECE    95\n",
            "\n",
            "Average Mark: 87.4\n",
            "\n",
            "Students scoring above 85:\n",
            "   RollNo    Name Department  Mark\n",
            "1     102    Bala        CSE    91\n",
            "3     104  Dinesh        CSE    88\n",
            "4     105   Ezhil        ECE    95\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "marks = pd.Series([85, 91, 78, 88, 95],\n",
        " index=[\"A\", \"B\", \"C\", \"D\", \"E\"])\n",
        "print(\"--- Pandas Series ---\")\n",
        "print(marks)\n",
        "data = {\n",
        " \"RollNo\": [101, 102, 103, 104, 105],\n",
        " \"Name\": [\"Anitha\", \"Bala\", \"Chitra\", \"Dinesh\", \"Ezhil\"],\n",
        " \"Department\": [\"CSE\", \"CSE\", \"ECE\", \"CSE\", \"ECE\"],\n",
        " \"Mark\": [85, 91, 78, 88, 95]\n",
        "}\n",
        "df = pd.DataFrame(data)\n",
        "print(\"\\n--- DataFrame ---\")\n",
        "print(df)\n",
        "print(\"\\nAverage Mark:\", round(df[\"Mark\"].mean(), 2))\n",
        "print(\"\\nStudents scoring above 85:\")\n",
        "print(df[df[\"Mark\"] > 85])\n"
      ]
    }
  ]
}