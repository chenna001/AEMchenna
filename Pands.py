{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ad65553e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                    mean    min    max\n",
      "                  Salary Salary Salary\n",
      "Department                            \n",
      "HR          46666.666667  40000  55000\n",
      "IT          60000.000000  50000  70000\n",
      "      Name      state  Salary\n",
      "4   Kesava  Bangalore   70000\n",
      "1      Bob        HYD   60000\n",
      "2  Charlie    chennai   40000\n",
      "                    mean    min    max\n",
      "                  Salary Salary Salary\n",
      "Department                            \n",
      "HR          46666.666667  40000  55000\n",
      "IT          60000.000000  50000  70000\n",
      "                    mean    min    max\n",
      "                  Salary Salary Salary\n",
      "Department                            \n",
      "HR          46666.666667  40000  55000\n",
      "IT          60000.000000  50000  70000\n",
      "     Name  Salary\n",
      "4  Kesava   70000\n",
      "               mean    min    max\n",
      "             Salary Salary Salary\n",
      "Department                       \n",
      "IT          60000.0  50000  70000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Alice\", \"Bob\", \"Charlie\", \"Chenna\", \"Kesava\", \"Reddy\"],\n",
    "    \"Department\": [\"IT\", \"IT\", \"HR\", \"HR\", \"IT\", \"HR\"],\n",
    "    \"Salary\": [50000, 60000, 40000, 45000, 70000, 55000],\n",
    "    \"state\": ['Bangalore','HYD','chennai','HYD','Bangalore','HYD']\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "result = pd.pivot_table(\n",
    "    df,\n",
    "    values=\"Salary\",\n",
    "    index=\"Department\",\n",
    "    aggfunc=[\"mean\", \"min\", \"max\"]\n",
    ")\n",
    "result2 = df[df[\"Department\"] == \"IT\"].loc[\n",
    "    lambda x: x[\"Salary\"] == x[\"Salary\"].max(),\n",
    "    [\"Name\", \"Salary\"]\n",
    "]\n",
    "result3 = df.loc[\n",
    "    df.groupby(\"state\")[\"Salary\"].idxmax(),\n",
    "    [\"Name\", \"state\", \"Salary\"]\n",
    "]\n",
    "#result4 = df.loc[\n",
    "   # df.groupby(\"State\")[\"Salary\"].idxmax(),\n",
    "   # [\"Name\", \"State\", \"Salary\"]\n",
    "#]\n",
    "\n",
    "print(result)\n",
    "print(result3)\n",
    "print(result)\n",
    "print(result)\n",
    "print(result2)\n",
    "#print(result4)\n",
    "print(result.loc[[\"IT\"]])\n",
    "#print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b9cd04dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name  Salary\n",
      "0    Alice   50000\n",
      "1      Bob   60000\n",
      "2  Charlie   40000\n",
      "3   Chenna   45000\n",
      "4   Kesava   70000\n",
      "5    Reddy   55000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Alice\", \"Bob\", \"Charlie\", \"Chenna\", \"Kesava\", \"Reddy\"],\n",
    "    \"Department\": [\"IT\", \"IT\", \"HR\", \"HR\", \"IT\", \"HR\"],\n",
    "    \"Salary\": [50000, 60000, 40000, 45000, 70000, 55000],\n",
    "    \"state\": ['Bangalore','HYD','chennai','HYD','Bangalore','HYD']\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df[[\"Name\", \"Salary\"]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e2614737",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>40000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Chenna</td>\n",
       "      <td>45000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kesava</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Reddy</td>\n",
       "      <td>55000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Salary\n",
       "0    Alice   50000\n",
       "1      Bob   60000\n",
       "2  Charlie   40000\n",
       "3   Chenna   45000\n",
       "4   Kesava   70000\n",
       "5    Reddy   55000"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[:, [\"Name\", \"Salary\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bc0741ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Name Department  Salary      state\n",
      "4  Kesava         IT   70000  Bangalore\n"
     ]
    }
   ],
   "source": [
    "result = df[df[\"Salary\"] > 60000]\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "18d26583",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Name Department  Salary      state   Bonus\n",
      "0   Alice         IT   50000  Bangalore  5000.0\n",
      "1     Bob         IT   60000        HYD  6000.0\n",
      "4  Kesava         IT   70000  Bangalore  7000.0\n",
      "5   Reddy         HR   55000        HYD  5500.0\n"
     ]
    }
   ],
   "source": [
    "#Below is the code to filter the rows where the salary is between 50000 and 70000.\n",
    "result = df[df[\"Salary\"].between(50000, 70000)]\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fc793e5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name Department  Salary      state   Bonus\n",
      "0    Alice         IT   50000  Bangalore  5000.0\n",
      "1      Bob         IT   60000        HYD  6000.0\n",
      "2  Charlie         HR   40000    chennai  4000.0\n",
      "3   Chenna         HR   45000        HYD  4500.0\n",
      "4   Kesava         IT   70000  Bangalore  7000.0\n",
      "5    Reddy         HR   55000        HYD  5500.0\n"
     ]
    }
   ],
   "source": [
    "#Bonus calculation.\n",
    "df[\"Bonus\"] = df[\"Salary\"] * 0.10\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e6ec6e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name Department  Salary      state   Bonus\n",
      "0    Alice         IT   60000  Bangalore  5000.0\n",
      "1      Bob         IT   70000        HYD  6000.0\n",
      "2  Charlie         HR   50000    chennai  4000.0\n",
      "3   Chenna         HR   55000        HYD  4500.0\n",
      "4   Kesava         IT   80000  Bangalore  7000.0\n",
      "5    Reddy         HR   65000        HYD  5500.0\n"
     ]
    }
   ],
   "source": [
    "#update the salary of all employees by adding 5000 to their current salary.\n",
    "df[\"Salary\"] = df[\"Salary\"] + 5000\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62907f68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name Department  Salary      state\n",
      "0    Alice         IT   60000  Bangalore\n",
      "1      Bob         IT   70000        HYD\n",
      "2  Charlie         HR   50000    chennai\n",
      "3   Chenna         HR   55000        HYD\n",
      "4   Kesava         IT   80000  Bangalore\n",
      "5    Reddy         HR   65000        HYD\n"
     ]
    }
   ],
   "source": [
    "#Drop the Bonus column from the DataFrame.\n",
    "df.drop(\"Bonus\", axis=1, inplace=True)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56834c91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name Department  Salary      state\n",
      "1      Bob         IT   70000        HYD\n",
      "2  Charlie         HR   50000    chennai\n",
      "3   Chenna         HR   55000        HYD\n",
      "4   Kesava         IT   80000  Bangalore\n",
      "5    Reddy         HR   65000        HYD\n"
     ]
    }
   ],
   "source": [
    "#Drop the first row from the DataFrame.\n",
    "df1=df.drop(0, axis=0)\n",
    "print(df1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5f063853",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name Department  Salary      state\n",
      "4   Kesava         IT   80000  Bangalore\n",
      "1      Bob         IT   70000        HYD\n",
      "5    Reddy         HR   65000        HYD\n",
      "0    Alice         IT   60000  Bangalore\n",
      "3   Chenna         HR   55000        HYD\n",
      "2  Charlie         HR   50000    chennai\n"
     ]
    }
   ],
   "source": [
    "#Sort the DataFrame by the \"Salary\" column in ascending order.\n",
    "df.sort_values(\"Salary\")\n",
    "ss=df.sort_values(\"Salary\", ascending=False)\n",
    "print(ss)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b23de42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0      ALICE\n",
      "1        BOB\n",
      "2    CHARLIE\n",
      "3     CHENNA\n",
      "4     KESAVA\n",
      "5      REDDY\n",
      "Name: Name, dtype: object\n"
     ]
    }
   ],
   "source": [
    "#Increase the salary of all employees by 10% using the apply() function.\n",
    "s=df[\"Name\"].str.upper()\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d8c36ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    66000.0\n",
      "1    77000.0\n",
      "2    55000.0\n",
      "3    60500.0\n",
      "4    88000.0\n",
      "5    71500.0\n",
      "Name: Salary, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "#Increase the salary of all employees by 10% using the apply() function.\n",
    "chenna=df[\"Salary\"] = df[\"Salary\"].apply(lambda x: x * 1.10)\n",
    "print(chenna)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "bf7e5646",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     79860.0\n",
      "1     93170.0\n",
      "2     66550.0\n",
      "3     73205.0\n",
      "4    106480.0\n",
      "5     86515.0\n",
      "Name: Salary, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "#Increase the salary of all employees by 10% using a custom function.\n",
    "def increase_salary(x):\n",
    "    return x * 1.10\n",
    "\n",
    "emp=df[\"Salary\"] = df[\"Salary\"].apply(increase_salary)\n",
    "print(emp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "99a7974b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Department\n",
      "HR    75423.333333\n",
      "IT    93170.000000\n",
      "Name: Salary, dtype: float64\n",
      "Department\n",
      "HR     86515.0\n",
      "IT    106480.0\n",
      "Name: Salary, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "#Group the DataFrame by the \"Department\" column and calculate the mean salary for each department.\n",
    "groupby=df.groupby(\"Department\")[\"Salary\"].mean()\n",
    "groupbt1=df.groupby(\"Department\")[\"Salary\"].max()\n",
    "print(groupby)\n",
    "print(groupbt1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d05f1b0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                    mean      min       max  count\n",
      "                  Salary   Salary    Salary Salary\n",
      "Department                                        \n",
      "HR          75423.333333  66550.0   86515.0      3\n",
      "IT          93170.000000  79860.0  106480.0      3\n"
     ]
    }
   ],
   "source": [
    "#Group the DataFrame by the \"Department\" column and calculate the mean, min, max, and count of salaries for each department using a pivot table.\n",
    "res = pd.pivot_table(\n",
    "    df,\n",
    "    values=\"Salary\",\n",
    "    index=\"Department\",\n",
    "    aggfunc=[\"mean\", \"min\", \"max\",'count']\n",
    ")\n",
    "\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "105f599c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                    mean      min       max\n",
      "Department                                 \n",
      "HR          75423.333333  66550.0   86515.0\n",
      "IT          93170.000000  79860.0  106480.0\n"
     ]
    }
   ],
   "source": [
    "# or Group the DataFrame by the \"Department\" column and calculate the mean, min, max, and count of salaries for each department using the groupby() method.\n",
    "multi=df.groupby(\"Department\")[\"Salary\"].agg(\n",
    "    [\"mean\", \"min\", \"max\"]\n",
    "    \n",
    ")\n",
    "print(multi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "3904ff81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Department</th>\n",
       "      <th>Salary</th>\n",
       "      <th>state</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Alice</th>\n",
       "      <td>IT</td>\n",
       "      <td>79860.0</td>\n",
       "      <td>Bangalore</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Bob</th>\n",
       "      <td>IT</td>\n",
       "      <td>93170.0</td>\n",
       "      <td>HYD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Charlie</th>\n",
       "      <td>HR</td>\n",
       "      <td>66550.0</td>\n",
       "      <td>chennai</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chenna</th>\n",
       "      <td>HR</td>\n",
       "      <td>73205.0</td>\n",
       "      <td>HYD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kesava</th>\n",
       "      <td>IT</td>\n",
       "      <td>106480.0</td>\n",
       "      <td>Bangalore</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Reddy</th>\n",
       "      <td>HR</td>\n",
       "      <td>86515.0</td>\n",
       "      <td>HYD</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Department    Salary      state\n",
       "Name                                   \n",
       "Alice           IT   79860.0  Bangalore\n",
       "Bob             IT   93170.0        HYD\n",
       "Charlie         HR   66550.0    chennai\n",
       "Chenna          HR   73205.0        HYD\n",
       "Kesava          IT  106480.0  Bangalore\n",
       "Reddy           HR   86515.0        HYD"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.set_index(\"Name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "83255ef6",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (2690195993.py, line 3)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[60]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mdf = pd.read_csv(r\"C:\\Users\\chenn\\Downloads\\country_list.csv\")\u001b[39m\n    ^\n\u001b[31mIndentationError\u001b[39m\u001b[31m:\u001b[39m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    " df = pd.read_csv(r\"C:\\Users\\chenn\\Downloads\\country_list.csv\")\n",
    "print(df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
