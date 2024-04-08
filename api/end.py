# from flask import Flask, jsonify, request
# from firebase.lost_and_found import db,retreive_all_found_items

# data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# @app.route('/dhruv')
# def hello_dhruv():
#     return 'Hello, Dhruv!'


# @app.route('/get_data', methods=['GET'])
# def get_data():
#     return jsonify(data)
# stored_data = {}
# req_data={}


# @app.route('/post_data', methods=['POST'])
# def post_data():
#     print('This is request: ',request)
#     req_data = request.get_json()
#     print("Hello aaryav, this is the data i got from fornt end",req_data)
    
#     matkd={'marks':5}
#     print('inside')
#     return jsonify(matkd)




# if __name__ == '__main__':
#     app.run(debug=True,host="0.0.0.0")