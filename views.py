from flask import jsonify, request
from flask import render_template
from models import Rasp
from models import Member

pis = [
    {'hostname': 'rasp1', 'ip': '168.10.10.05', 'serial': 'fbca35caf3'},
    {'hostname': 'rasp2', 'ip': '168.10.10.06', 'serial': 'fbca35caf3'},
    {'hostname': 'rasp3', 'ip': '168.10.10.07', 'serial': 'fbca35caf3'}
]


# no additional rout
# @app.route('/')
def index():
    return render_template('index.html')


# @app.route('/pilist')
def get_all_pis():
    return jsonify(pis)


# @app.route('/savepi/<hostname>')
def save_pi(hostname):
    pis.append({'hostname': hostname, 'ip': '168.10.10.10', 'serial': 'fbca35caf3'})
    return "saved"


# @app.route('/savepi_2', methods=['GET', 'POST'])
def save_pi_2():
    hostname = request.args.get('hostname')
    serial = request.args.get('serial')
    pis.append({'hostname': hostname, 'ip': '168.10.10.10', 'serial': serial})
    return "saved"


def add_member():
    name = request.values.get('name')
    email = request.values.get('email')

    # TODO check if member in collection
    if name:
        member = Member(name=name, email=email)
        member.save()
        return f"Member by {name} was added. ({email})"
    else:
        return "Member must be set with name as a post argument. Member was not saved"

# @app.route('/add_rasp')
def add_rasp():
    serial = request.args.get('serial')
    rasp = Rasp(serial=serial)
    rasp.wlan = '0.0.0.0'
    rasp.save()
    return "rasp  was added"


# @app.route('/rasps')
def show_rasps():
    # Rasp.objects.all()
    return render_template('show.html', raspberries=Rasp.objects.all())


def show_members():
    return render_template('show_members.html', members=Member.objects.all())
