from flask import render_template,redirect,Blueprint,request,url_for,jsonify
from dbconfig import db
from models import EnergyType,Area,EnergyDevice
from sqlalchemy import or_, cast
from sqlalchemy.types import String
import re

energy_bp = Blueprint('energy', __name__)

@energy_bp.route('/addact', methods=['GET', 'POST'])
def addact():
    if request.method == 'POST':
        deviceid = request.form['deviceid']
        areaid = request.form['areaid']
        energyid = request.form['energyid']
        new_device = EnergyDevice(DeviceID=deviceid, AreaID=areaid, EnergyID=energyid)
        db.session.add(new_device)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addact.html')

@energy_bp.route('/editact/<int:id>',methods=['GET', 'POST'])
def editact(id):
    device = EnergyDevice.query.get_or_404(id)
    if request.method == 'POST':
        device.DeviceID = request.form['deviceid']
        device.AreaID = request.form['areaid']
        device.EnergyID = request.form['energyid']

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('editact.html', device=device)

@energy_bp.route('/deleteact/<int:id>')
def deleteact(id):
    device = EnergyDevice.query.get_or_404(id)
    db.session.delete(device)
    db.session.commit()
    return redirect(url_for('home'))

@energy_bp.route('/search')
def search():
    search_term = request.args.get('search_content')
    # if search_term:
    #     devices = EnergyDevice.query.filter(
    #     or_(
    #         cast(EnergyDevice.DeviceID, String).ilike(f"%{search_term}%"),
    #         cast(EnergyDevice.AreaID, String).ilike(f"%{search_term}%"),
    #         cast(EnergyDevice.EnergyID, String).ilike(f"%{search_term}%")
    #     )
    # ).all()
    if search_term:
        # 根据输入内容判断查询字段
        if search_term.startswith("Area") or search_term.startswith("Area-"):
            # 如果输入以 "Area" 或 "Area-" 开头，查询 AreaID
            clean_search_term = search_term.replace("Area", "").replace("-", "").strip()  # 去掉前缀或符号
            devices = EnergyDevice.query.filter(
                cast(EnergyDevice.AreaID, String).ilike(f"%{clean_search_term}%")
            ).all()
        elif search_term.startswith("Energy") or search_term.startswith("Energy-"):
            # 如果输入以 "Energy" 或 "Energy-" 开头，查询 EnergyID
            clean_search_term = search_term.replace("Energy", "").replace("-", "").strip()  # 去掉前缀或符号
            devices = EnergyDevice.query.filter(
                cast(EnergyDevice.EnergyID, String).ilike(f"%{clean_search_term}%")
            ).all()
        elif search_term.startswith("ID") or search_term.startswith("ID-"):
            # 如果输入以 "ID" 或 "ID-" 开头，查询 ID
            clean_search_term = search_term.replace("ID", "").replace("-", "").strip()  # 去掉前缀或符号
            devices = EnergyDevice.query.filter(
                cast(EnergyDevice.DeviceID, String).ilike(f"%{clean_search_term}%")
            ).all()
        else:
            # 如果无法判断，默认在所有字段中模糊查询
            devices = EnergyDevice.query.filter(
                or_(
                    cast(EnergyDevice.DeviceID, String).ilike(f"%{search_term}%"),
                    cast(EnergyDevice.AreaID, String).ilike(f"%{search_term}%"),
                    cast(EnergyDevice.EnergyID, String).ilike(f"%{search_term}%")
                )
            ).all()
    else:
        devices = EnergyDevice.query.all()

        # 只返回表格部分的渲染结果
    return render_template('_device_table.html', devices=devices)

