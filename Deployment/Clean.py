def Cleaning(df):
    """ Cleans raw dataset for Preprocessing
    
    input: A Dataframe that has the keys:
        ['Survived', 'Pclass', 'Name',
        'Sex', 'Age', 'SibSp', 'Parch', 
        'Ticket','Fare', 'Cabin', 'Embarked']
        
    returns Cleaned Dataset with no Business outliers or np.nan if no entries remained."""

    df = df.rename(columns={
        'Pclass':'Ticket_class',
        'SibSp' :'Siblings_Spouses',
        'Parch' :'Parents_Children',
    })

    df['Survived'] = df['Survived'].map({0:'No',1:'Yes'})
    # df['Ticket_class'] = df['Ticket_class'].map({1:'1st',2:'2nd',3:'3rd'})
    df['Embarked'] = df['Embarked'].map({
        'C':'Cherbourg',
        'Q':'Queenstown',
        'S': 'Southampton'
    })

    df['Sex'] = df.Sex.apply(lambda x: x.capitalize())
    
    df.drop('Cabin',axis = 1, inplace = True)
    df.drop('Ticket',axis = 1,inplace = True)
    df.drop('Name',axis = 1, inplace = True)
    df.dropna(inplace = True)
    df['Age'] = df.Age.astype('int')
    df.drop(df[(df['Fare'] > 300) | (df['Fare'] <= 0)].index,inplace = True)
    
    if df.shape[0] == 0:
        return np.nan
    else:
        return df