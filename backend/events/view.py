from flask import Blueprint,Flask,render_template,session,request,jsonify,make_response,session
from backend.db.Events import query_events,query_by_id,remove_event
from backend.users.auth import adminRequired,login_required



event_blueprint = Blueprint(
    'event',
    __name__,
    template_folder='templates'
)


@event_blueprint.route("/all")
@login_required
def all_events():
    try:
        data = query_events()
        return(jsonify({"events":data}))
    except:
        return (jsonify({"error":"There was an error retriving data!"})),500


@event_blueprint.route("/view/<id>")
@adminRequired
def view_by_id(id):
    try:

        data = query_by_id(id)
        event = {"created_by":data.Created_By,"event_title":data.Event_Title,'date_start':data.Date_Start,"datEe_end":data.Date_End,'time_start':data.Time_Start,
        "time_end":data.Time_End,'location':data.Location}
       
        return (jsonify({"event":event}))
    except Exception as e:
        print(e)
        return(jsonify({"error":"There was an error retriving data!"})),500


@event_blueprint.route("/delete/<id>",methods=["DELETE"])
@adminRequired
def delete(id):
    try:
        remove_event(id)
        return (jsonify({"success":"Event removed successfully!"}))
    except Exception as e:
        print(e)
        return ("There was an error deleting this event, please verify the event ID matches the event you are trying to delete!"),500








  