from itertools import chain
import tkinter as tk

from tkinter import ttk, filedialog

import PIL.Image
import PIL.ImageTk

from . import __version__
from .config import Config
from .wfc import WFC


class ConfigFrame(ttk.Notebook):
    def __init__(self, master, *configs: Config) -> None:
        super().__init__(master)
        self.columnconfigure(0, weight=1)

        self.configs = {i.name: i for i in configs}

        self._cfg_base_frame = ttk.Frame(self, padding=(1.5, 3, 1.5, 3))
        self.add(self._cfg_base_frame, text='Base')
        self._cfg_base_frame.columnconfigure(0, weight=1)
        self._cfg_base_frame.columnconfigure(1, weight=1)

        self._cfg = ttk.Combobox(self._cfg_base_frame, state='readonly', values=tuple(self.configs.keys()))
        self._cfg.grid(column=0, row=0, columnspan=2, sticky='NEW', padx=1.5)
        self._cfg.bind('<<ComboboxSelected>>', self._cfg_select)

        self._size_frame = ttk.LabelFrame(self._cfg_base_frame, text='size', padding=(3, 3, 3, 3))
        self._size_frame.grid(column=0, row=1, sticky='NEW', padx=1.5)
        self._size_frame.columnconfigure(1, weight=1)

        self._size_x_label = ttk.Label(self._size_frame, text='X:')
        self._size_x_label.grid(column=0, row=0, sticky=tk.E)

        self._size_width = ttk.Spinbox(self._size_frame, width=5, from_=1, to=99999, command=self._change_size)
        self._size_width.grid(column=1, row=0, sticky=tk.EW)
        self._size_width.bind('<Return>', self._change_size)

        self._size_y_label = ttk.Label(self._size_frame, text='Y:')
        self._size_y_label.grid(column=0, row=1, sticky=tk.E)

        self._size_height = ttk.Spinbox(self._size_frame, width=5, from_=1, to=99999, command=self._change_size)
        self._size_height.grid(column=1, row=1, sticky=tk.EW)
        self._size_height.bind('<Return>', self._change_size)

        self._tile_size_frame = ttk.LabelFrame(self._cfg_base_frame, text='tile size', padding=(3, 3, 3, 3))
        self._tile_size_frame.grid(column=1, row=1, sticky='NEW', padx=1.5)
        self._tile_size_frame.columnconfigure(1, weight=1)

        self._tile_size_x_label = ttk.Label(self._tile_size_frame, text='X:')
        self._tile_size_x_label.grid(column=0, row=0, sticky=tk.E)

        self._tile_size_width = ttk.Spinbox(self._tile_size_frame, width=5, from_=1, to=99999, command=self._change_tile_size)
        self._tile_size_width.grid(column=1, row=0, sticky=tk.EW)
        self._tile_size_width.bind('<Return>', self._change_tile_size)

        self._tile_size_y_label = ttk.Label(self._tile_size_frame, text='Y:')
        self._tile_size_y_label.grid(column=0, row=1, sticky=tk.E)

        self._tile_size_height = ttk.Spinbox(self._tile_size_frame, width=5, from_=1, to=99999, command=self._change_tile_size)
        self._tile_size_height.grid(column=1, row=1, sticky=tk.EW)
        self._tile_size_height.bind('<Return>', self._change_tile_size)

        self._cfg_advanced_frame = ttk.Frame(self, padding=(3, 3, 3, 3))
        self.add(self._cfg_advanced_frame, text='Advanced')
        # self._cfg_advanced_frame.columnconfigure(0, weight=1)
        # self._cfg_advanced_frame.columnconfigure(1, weight=1)

        self._starter_points_label = ttk.Label(self._cfg_advanced_frame, text='Starter Points:')
        self._starter_points_label.grid(column=0, row=0, sticky=tk.E)

        self._starter_points = ttk.Spinbox(self._cfg_advanced_frame, width=5, from_=1, to=999999999, command=self._change_starter_points)
        self._starter_points.grid(column=1, row=0, sticky=tk.EW)
        self._starter_points.bind('<Return>', self._change_starter_points)

        self._set_state(tk.DISABLED)

    def get_config(self, force=False) -> Config:
        if force:
            self._change_size()
            self._change_tile_size()
            self._change_starter_points()
        return self.configs[self._cfg.get()]

    def _cfg_select(self, event: tk.Event = None) -> None:
        cfg = self.get_config()

        # base
        self._size_width.set(cfg.size[0])
        self._size_height.set(cfg.size[1])
        self._tile_size_width.set(cfg.tile_size[0])
        self._tile_size_height.set(cfg.tile_size[1])

        # advanced
        self._starter_points.set(cfg.starter_points)

        self._set_state(tk.NORMAL)
        self.event_generate('<<ConfigSelected>>')

    def disable(self):
        self._cfg.configure(state=tk.DISABLED)
        self._set_state(tk.DISABLED)

    def enable(self):
        self._cfg.configure(state=tk.NORMAL)
        self._set_state(tk.NORMAL)

    def _set_state(self, state) -> None:
        self.tab(1, state=state)
        for child in chain(self._size_frame.children.values(),
                           self._tile_size_frame.children.values(),
                           self._cfg_advanced_frame.children.values()):
            self._elem_set_state(child, state)

    @staticmethod
    def _elem_set_state(elem, state) -> None:
        try:
            for child in elem.children.values():
                try:
                    child.configure(state=state)
                except:
                    pass
        except:
            pass
        try:
            elem.configure(state=state)
        except:
            pass

    @staticmethod
    def _constrain(val, max_=99999):
        return min(int(val), int(max_))

    def _change_size(self, e=None) -> None:
        cfg = self.get_config()
        cfg.size = self._constrain(self._size_width.get()), self._constrain(self._size_height.get())
        self._size_width.set(cfg.size[0])
        self._size_height.set(cfg.size[1])

    def _change_tile_size(self, e=None) -> None:
        cfg = self.get_config()
        cfg.tile_size = self._constrain(self._tile_size_width.get()), self._constrain(self._tile_size_height.get())
        self._tile_size_width.set(cfg.tile_size[0])
        self._tile_size_height.set(cfg.tile_size[1])

    def _change_starter_points(self, e=None) -> None:
        cfg = self.get_config()
        cfg.starter_points = self._constrain(self._starter_points.get(), cfg.size[0] * cfg.size[1])
        self._starter_points.set(cfg.starter_points)


class App(ttk.Frame):
    def __init__(self, *configs: Config) -> None:
        super().__init__()
        self.master.protocol("WM_DELETE_WINDOW", self._exit)
        self.master.option_add('*tearOff', tk.FALSE)

        self.master.title('Wave Function Collapse')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.grid(column=0, row=0, sticky=tk.NSEW)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self._menubar = tk.Menu(self)
        self.master['menu'] = self._menubar

        self._menu_file = tk.Menu(self._menubar)
        self._menubar.add_cascade(menu=self._menu_file, label='File', underline=0)
        self._menu_file.add_separator()
        self._menu_file.add_command(label='Exit', accelerator='Ctrl-Q', command=self._exit, underline=1)
        self.master.bind('<Control-Q>', self._exit)
        self.master.bind('<Control-q>', self._exit)

        self._menu_help = tk.Menu(self._menubar, name='help')
        self._menubar.add_cascade(menu=self._menu_help, label='Help', underline=0)
        self._menu_help.add_separator()
        self._menu_help.add_command(label='About...', accelerator='F1', command=self._about, underline=0)
        self.master.bind('<F1>', self._about)

        # Control Frame
        self._ctrl_frame = ttk.Frame(self, padding=(3, 3, 3, 3))
        self._ctrl_frame.grid(column=0, row=0, sticky=tk.NSEW)

        self._cfg_frame = ConfigFrame(self._ctrl_frame, *configs)
        self._cfg_frame.grid(column=0, row=0, sticky='NEW', columnspan=3)
        self._cfg_frame.bind('<<ConfigSelected>>', self._cfg_select)

        self._start_btn = ttk.Button(self._ctrl_frame, text='Start', state=tk.DISABLED, command=self._start)
        self._start_btn.grid(column=0, row=1, sticky=tk.N, pady=3)

        self._stop_btn = ttk.Button(self._ctrl_frame, text='Stop', state=tk.DISABLED, command=self._stop)
        self._stop_btn.grid(column=1, row=1, sticky=tk.N, pady=3)

        self._save_btn = ttk.Button(self._ctrl_frame, text='Save', state=tk.DISABLED, command=self._save_result)
        self._save_btn.grid(column=2, row=1, sticky=tk.N, pady=3)

        self._autorestart = tk.BooleanVar(value=True)
        self._autorestart_chkbox = ttk.Checkbutton(self._ctrl_frame, text='Auto-restart on error', variable=self._autorestart)
        self._autorestart_chkbox.grid(column=0, row=2, sticky=tk.W, columnspan=3)

        self._progress_bar = ttk.Progressbar(self._ctrl_frame, orient=tk.HORIZONTAL, mode='determinate')
        self._progress_bar.grid(column=0, row=3, sticky='NEW', columnspan=3, pady=3)

        # Canvas Frame
        self._canvas_frame = ttk.Frame(self)
        self._canvas_frame.grid(column=1, row=0, sticky=tk.NSEW)
        self._canvas_frame.columnconfigure(0, weight=1)
        self._canvas_frame.rowconfigure(0, weight=1)

        self._canvas_scroll_h = ttk.Scrollbar(self._canvas_frame, orient=tk.HORIZONTAL)
        self._canvas_scroll_h.grid(column=0, row=1, sticky=tk.EW)
        self._canvas_scroll_v = ttk.Scrollbar(self._canvas_frame, orient=tk.VERTICAL)
        self._canvas_scroll_v.grid(column=1, row=0, sticky=tk.NS)

        self._canvas = tk.Canvas(self._canvas_frame, yscrollcommand=self._canvas_scroll_v.set, xscrollcommand=self._canvas_scroll_h.set)
        self._canvas.grid(column=0, row=0, sticky=tk.NSEW)
        self._canvas_scroll_h.configure(command=self._canvas.xview)
        self._canvas_scroll_v.configure(command=self._canvas.yview)

        self.update()
        self.master.minsize(self.winfo_width(), self.winfo_height())

        self._wfc = WFC()

    def _cfg_select(self, event: tk.Event) -> None:
        self._start_btn.configure(state=tk.NORMAL)
        self._save_btn.configure(state=tk.NORMAL)

    def _start(self):
        self._start_btn.configure(state=tk.DISABLED)
        self._stop_btn.configure(state=tk.NORMAL)
        self._save_btn.configure(state=tk.DISABLED)
        self._cfg_frame.disable()

        cfg = self._cfg_frame.get_config(force=True)

        for t in cfg.tiles:
            setattr(t, 'tki', [None] * len(t.images))

        self._wfc.configure(cfg)
        self._progress_bar.configure(maximum=(self._wfc.width * self._wfc.height))
        self._canvas.configure(scrollregion=(0, 0, cfg.size[0] * cfg.tile_size[0], cfg.size[1] * cfg.tile_size[1]))
        x = y = 0

        while 1:
            self._progress_bar.configure(value=0)
            self._progress_bar.update()
            self._canvas.delete(tk.ALL)
            self._canvas.create_rectangle(0, 0, cfg.size[0] * cfg.tile_size[0], cfg.size[1] * cfg.tile_size[1], fill='black')
            rect = self._canvas.create_rectangle(0, 0, cfg.tile_size[0], cfg.tile_size[1], outline='#b00', width=2)

            for x, y, s, idx in self._wfc.run():
                if idx >= 0:
                    t = cfg.tiles[s]
                    if t.tki[idx] is None:
                        t.tki[idx] = PIL.ImageTk.PhotoImage(t.images[idx])
                    self._canvas.create_image(x, y, anchor=tk.NW, image=t.tki[idx])
                    self._progress_bar.step(1)
                self._canvas.coords(rect, x, y, x + cfg.tile_size[0], y + cfg.tile_size[1])
                self._canvas.tag_raise(rect)
                self.update()

            if self._wfc.done == 1:
                break
            elif self._wfc.done == -1 and not self._autorestart.get():
                break

        self._canvas.delete(tk.ALL)
        self._imgtk = PIL.ImageTk.PhotoImage(self._wfc.result)
        self._canvas.create_image(0, 0, anchor=tk.NW, image=self._imgtk)
        if self._wfc.done == -1:
            self._canvas.create_rectangle(x, y, x + cfg.tile_size[0], y + cfg.tile_size[1], outline='#b00', width=2)

        self._cfg_frame.enable()
        self._start_btn.configure(state=tk.NORMAL)
        self._stop_btn.configure(state=tk.DISABLED)
        self._save_btn.configure(state=tk.NORMAL)

    def _stop(self):
        self._wfc.done = 1

    def _save_result(self):
        filepath = filedialog.asksaveasfilename(filetypes=[('images', ['*.png', '*.jpg', '*.bmp'])])
        if filepath:
            self._wfc.save_result(filepath)

    def _exit(self, evt=None):
        self._stop()
        self.quit()

    def _about(self, evt=None):
        # dialog.Dialog(self, title='About', text='Some text', bitmap=dialog.DIALOG_ICON, default=0, strings=('Ok',))
        # messagebox.showinfo('About', 'Some text', master=self)
        about = tk.Toplevel(self)
        about.title('About')
        ttk.Label(about, text=f'Version: {__version__}').grid()
        ttk.Button(about, text='Ok', command=lambda: (about.grab_release(), about.destroy())).grid()
        about.transient(self)
        about.wait_visibility()
        about.grab_set()
        # about.wait_window()
