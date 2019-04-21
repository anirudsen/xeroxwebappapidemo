from server import app, request, jsonify
from resource.db import cursor

@app.route('/asset')
@app.route('/asset/<asset_id>')
def getAssetByID(asset_id=None):

    cursor.execute(
        'SELECT Id,FullName, UserName, Email, Password, Avatar FROM [TechnologyApp].[Users]')
    row = cursor.fetchone()

    assets = []

    while row:
        asset = {
            'Id': row[0],
            'FullName': row[1],
            'UserName': row[2],
            'Email': row[3],
            'Password': row[4],
            'Avatar': row[5]
        }
        assets.append(asset)
        row = cursor.fetchone()

    # print(f'Value: {user_id}')
    # print(request.args.get('username'))
    return jsonify(assets)

